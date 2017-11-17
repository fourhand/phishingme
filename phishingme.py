import requests
import hashlib
import time
import random

for _index in range(1, 100):
    hash_object = hashlib.md5(b'Hello World')
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'b', 'c', 'd', 'e']
    randomhex = ''
    for _index2 in range(1, 32):
        randomhex = randomhex + random.choice(hex)
    URL = 'http://phishingme.kt.co.kr:8080/' + randomhex + '.raf'
    print(URL)
    res = requests.get(URL)
    print('===================================')
    print(res.status_code)
    print(res.text)
    time.sleep(0.5)



