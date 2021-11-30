#!/usr/bin/python
import sys
from bs4 import BeautifulSoup
import re

with open(str(sys.argv[1]), 'r', encoding="utf8") as file:
    data = file.read()
file_name = re.sub(r"[.\\]|gpx", '', str(sys.argv[1]))
bs_data = BeautifulSoup(data, 'xml')
xml_caches = bs_data.find_all('wpt')
with open(file_name+'_codes.txt', 'w', encoding="utf8") as file:
    for cache in xml_caches:
        gc_code = cache.find('name').text
        gc_name = cache.find('desc').text
        gc_url = cache.find('url').text if cache.find('url') != None else ''
        lat = float(cache.get('lat'))
        lon = float(cache.get('lon'))
        lat_degrees = int(lat)
        lat_minutes = (lat % 1)*60
        lon_degrees = int(lon)
        lon_minutes = (lon % 1)*60
        formatted_string = "{gc_code} {gc_name} {gc_url} N{lat_degrees:d}° {lat_minutes:5.3f}' E{lon_degrees:03d}° {lon_minutes:5.3f}'".format(
            gc_code=gc_code, gc_name=gc_name, gc_url=gc_url, lat_degrees=lat_degrees, lat_minutes=lat_minutes, lon_degrees=lon_degrees, lon_minutes=lon_minutes)
        file.write(formatted_string)
