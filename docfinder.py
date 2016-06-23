''' Keyword-searchable document database

API:
    create_db(force=False) --> None
    add_document(uri, text) --> None
    get_document(uri) --> text
    search(*keywords) --> uris ordered by relevance

    Exceptions: DuplicateURI, UnknownURI


Tables:

    Documents
    ================
    uri         text  <-- unique index
    content     blob

    Keywords
    ================
    term        text  <-- index
    uri         text
    score       real

'''

from __future__ import division
from collections import Counter
from contextlib import closing
import re, sqlite3, bz2, os

__all__ = ['create_db', 'add_document', 'get_document', 'search',
           'DuplicateURI', 'UnknownURI']


stopwords = {'and', 'or', 'is', 'of', 'the', 'a', 'for', 'in', 'be', 'that', 'be'}

database = 'pepsearch.db'


class DuplicateURI(Exception):
    'URI already present in database'

class UnknownURI(KeyError):
    'URI not found in database'

def create_db(force=False):
    '''
    Create a new document database.
    Delete the existing one if ``force==True``.
    '''
    if force:
        try:
            os.remove(database)
        except OSError:
            pass # database does not exist, yet

    with closing(sqlite3.connect(database)) as connection:
          c = connection.cursor()
          c.execute('CREATE TABLE Documents (uri text, content blob)')
          c.execute('CREATE UNIQUE INDEX KeyIndex ON Documents (uri)')
          c.execute('CREATE TABLE keywords (term text, uri text, score real)')
          c.execute('CREATE INDEX KeyIndex ON Keywords (term)')

def normalize(words):
    '''
    Lowercase, de-pluralize, and ignore stopwords.

        >>> list(normalize(['Hettinger', 'enumerates', 'AND']))
        ['hettinger', 'enumerate']
    ''' # Use NLTK for more sophisticated normalization
    for word in words:
        word = word.lower()
        if word not in stopwords:
            yield word.rstrip('s')


def score_document(text, pattern=r'[A-Za-z]+', n=200):
    '''
    Calculate the relevance scores for the
    ``n`` most frequent terms in the document.
    '''
    words = re.findall(pattern, text)
    terms = list(normalize(words))
    total = len(terms)
    counts = Counter(terms)
    for term, count in counts.most_common(n):
        score = count / total
        yield term, score
    

def add_document(uri, text):
    '''
    Insert a new document into the database.
    '''
    # Score terms and compress document before storing.
    # May raise DuplicateURI.


def get_document(uri):
    '''
    Retrieve a document from the database with specified URI.
    '''
    # May raise UnknownURI


def search(*keywords):
    '''
    Find the URIs of documents relevant to the specified keywords.
    '''

