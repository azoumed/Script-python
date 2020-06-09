#!/bin/env python3
# -*- coding:utf8 -*-

import redis
r1 = redis.Redis(host="rcnpdiot.redis.cache.windows.net", db=1, password="gYvKz+5xP1OEBdFTRUKlRAoAv1oxuy86nTKRTnokVnk=", port=6380, ssl=True)
r2 = redis.Redis(host="rcnpdiot.redis.cache.windows.net", db=2, password="gYvKz+5xP1OEBdFTRUKlRAoAv1oxuy86nTKRTnokVnk=", port=6380, ssl=True)

#print(r1.keys())
def parcour(rdb:redis.Redis):
    for key in rdb.scan_iter():
        print(key)

#r1.client_getname
#r1.get