# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:10:29 2017

@author: mashiksa
"""
xml Documents : https://docs.python.org/2/library/xml.etree.elementtree.html
	
#Example XML File 
#
#<CATALOG>
#    <CD>
#        <TITLE>Empire Burlesque</TITLE>
#        <ARTIST>Bob Dylan</ARTIST>
#        <COUNTRY>USA</COUNTRY>
#        <COMPANY>Columbia</COMPANY>
#        <PRICE>10.90</PRICE>
#        <YEAR>1985</YEAR>
#    </CD>
#    <CD>
#        <TITLE>Hide your heart</TITLE>
#        <ARTIST>Bonnie Tylor</ARTIST>
#        <COUNTRY>UK</COUNTRY>
#        <COMPANY>CBS Records</COMPANY>
#        <PRICE>9.90</PRICE>
#        <YEAR>1988</YEAR>
#    </CD>
#</CATALOG>

import xml.etree.cElementTree as ET
xmldoc = ET.parse('cd_catalog.xml')
root = xmldoc.getroot()
rootlist = root.findall('CD')
doc = {}
item_id = 0

for item in root.findall('CD'):
	item_dic = {}
	item_dic['title'] = item.find('TITLE').text
	item_dic['artist'] = item.find('ARTIST').text
	item_dic['country'] = item.find('COUNTRY').text
	item_dic['price'] = float(item.find('PRICE').text)
	item_dic['year'] = int(item.find('YEAR').text)
	item_id += 1
	doc["id_" + str(item_id)] = item_dic