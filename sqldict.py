
'''
dict-like object, backed by a SQLite database.

- persistence
- concurrency
- shareable with other languages
- backups are easy, because it's a single file


We will use the MutableMapping ABC as our prefab building.
We are responsible for pouring the foundation:
    __getitem__, __setitem__, __delitem__, __iter__, and __len__
We get all the other tools connected to our foundation.
'''

from collections import MutableMapping
import sqlite3, json


class SqlDict(MutableMapping):
    'dict-like, backed by a SQLite database'

    def __init__(self, dbname, *args, **kwargs):
        self.dbname = dbname
        self.connection = sqlite3.connect(dbname)
        c = self.connection.cursor()
        try:
            c.execute('CREATE TABLE Dict (key text, value text)')
            c.execute('CREATE UNIQUE INDEX KeyIndex ON Dict (key)')
        except sqlite3.OperationalError:
            pass # table already exists
        self.update(*args, **kwargs)

    def __repr__(self):
        return 'SqlDict(%r, %r)' % (self.dbname, self.items())
        
    def __getitem__(self, key):
        c = self.connection.cursor()
        c.execute('SELECT value FROM Dict WHERE key=?', (key,))
        row = c.fetchone()
        if row is None:
            raise KeyError(key)
        return json.loads(row[0])

    def __setitem__(self, key, value):
        if key in self:     # LBYL causes a race condition
            del self[key]   # TODO: use better SQL to stop the race
        c = self.connection.cursor()
        c.execute('INSERT INTO Dict VALUES (?, ?)', (key, json.dumps(value)))
        self.connection.commit()

    def __delitem__(self, key):
        if key not in self:
            raise KeyError(key)
        c = self.connection.cursor()
        c.execute('DELETE FROM Dict WHERE key=?', (key,))
        self.connection.commit()

    def __len__(self):
        c = self.connection.cursor()
        c.execute('SELECT count(key) FROM Dict')
        row = c.fetchone()
        return row[0]

    def __iter__(self):
        c = self.connection.cursor()
        c.execute('SELECT key FROM Dict')
        rows = c.fetchall()
        return iter([key for (key,) in rows])

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, etype, e, traceback):
        self.close()


if __name__ == '__main__':
    with SqlDict('starwars2.db') as d:
        d['hero'] = 'Luke'
        d['villain'] = 'Darth'
        print d
        del d['villain']
        d['hero'] = ('Rey', 'Finn')
        print d
