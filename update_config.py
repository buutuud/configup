# -*- coding: utf-8 -*-
# @Author: happyyi
# @Date:   2017-07-30 21:17:26
# @Last Modified by:   happyyi
# @Last Modified time: 2017-07-30 21:55:02
import requests
import os
if os.path.isfile('config.json'):
    os.remove("config.json")
    print r'01.Del Old Config File'

print r'02.Downloading New Config File'
url = "http://oqkhan93s.bkt.clouddn.com/config.json"
r = requests.get(url)
dat = r.content
print dat
if dat.find('Document not found') != -1:
    print r'03.Download New Config File Failed'
else:
    f = open('config.json', 'wb')
    f.write(r.content)
    f.close()
    print r'03.Download New Config File Succeed'
os.system("pause")
