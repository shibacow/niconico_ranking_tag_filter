#!/usr/bin/python
# -*- coding:utf-8 -*-
import json
import urllib2
from xml.etree.ElementTree import ElementTree
import re
xmlsrc='http://www.nicovideo.jp/ranking/fav/daily/all?rss=2.0'

def parseXML(url,sminfos):
    xml=ElementTree(file=urllib2.urlopen(url))
    for e in xml.findall('.//item'):
        elmdict={}
        for t in e.iter():
            if t.tag=='title':
                elmdict['title']=t.text
            elif t.tag=='link':
                link=t.text
                smid=re.findall('http://www.nicovideo.jp/watch/(.*)',link)[0]
                elmdict['link']=link
                elmdict['smid']=smid
            elif t.tag=='description':
                desc=t.text
                imgs=re.findall('<img (.*)/>',desc)[0]
                thumb=re.findall('src="(.*?)"',imgs)[0]
                alt=re.findall('alt="(.*?)"',imgs)[0]
                elmdict['thumb']=thumb
                elmdict['alt']=alt
        sminfos.append(elmdict)

def readRanking():
    smids=[]
    for i in range(1,4):
        url=xmlsrc+'&page=%d' % i
        parseXML(url,smids)
    return smids

def generateJSON(result):
    print 'Content-type: application/json\r\n'
    s=json.dumps(result)
    print s

sminfos=readRanking()
generateJSON(sminfos)
