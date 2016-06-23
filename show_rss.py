# show_rss.py

filename = 'notes/rss.xml'

import xml.etree.ElementTree as ET

tree = ET.parse(filename)
root = tree.getroot()

for item in root.findall('channel/item'):
    title = item.find('title').text
    pubDate = item.find('pubDate').text
    print "%s [%s]" % (title, pubDate)
