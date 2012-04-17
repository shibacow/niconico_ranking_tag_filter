#!/usr/bin/python
# -*- coding:utf-8 -*-
import json
import re
import anydbm
from datetime import datetime


def getKeys():
    f=datetime.now().strftime('%Y-%m-%d')+'.db'
    db=anydbm.open(f,'r')
    tags=[]
    for t in db.keys():
        ls=db[t]
        sz=len(json.loads(ls))
        k=unicode(t,'utf-8')
        tags.append((k,sz))
    tags=sorted(tags,key=lambda x:x[1],reverse=True)
    return tags[:80]

def generateJSON(result):
    print 'Content-type: application/json\r\n'
    s=json.dumps(result)
    print s
keys=getKeys()
generateJSON(keys)
