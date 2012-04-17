#!/usr/bin/python
# -*- coding:utf-8 -*-
import json
import urllib2
import re
import anydbm
from datetime import datetime
import cgi,os
query={}
query_key='QUERY_STRING'
if query_key in os.environ:
    query=cgi.parse_qs(os.environ[query_key])

def searchWord(query):
    q=query['word'][0]
    f=datetime.now().strftime('%Y-%m-%d')+'.db'
    db=anydbm.open(f,'r')
    if db.has_key(q):
        v=db[q]
        return json.loads(v)
    return []
def generateJSON(result):
    print 'Content-type: application/json\r\n'
    s=json.dumps(result)
    print s
smids=searchWord(query)
generateJSON(smids)
