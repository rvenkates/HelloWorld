# show_weather.py
 
import datetime
import time
import urllib
import json
from xml.etree.ElementTree import parse
 
root_url_template = 'http://w1.weather.gov/xml/current_obs/%s.xml'
locations = 'KSJC', 'KJFK', 'KEWR', 'KDFW', 'KSFO'
w_measurements = {}
for _ in range(10):
    now = str(datetime.datetime.now())
    l_measurements = []
    for location in locations:
        url = root_url_template % location
        u = urllib.urlopen(url)
        root = parse(u).getroot()
        l_measurements.append({location : (root.find('temperature_string').text, root.find('relative_humidity').text)})
    w_measurements[now] = l_measurements
    time.sleep(0.1);


print json.dumps(w_measurements, indent=1)

