#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import json
import urllib2
import os
import urllib
import sys
import StringIO
import peewee
import datetime
import ccdb

def returnFilehandleFromInputStr(input_str):
    if "http" in input_str:
        urls = StringIO.StringIO(input_str)
    else:
        if __name__ == '__main__':
            urls = open(input_str)
        else:
            urls = StringIO.StringIO(input_str)
    return urls

def returnDownloadImageCV2(url):
    resp = urllib.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def goCheck(input_str):
    fh = returnFilehandleFromInputStr(input_str)
    dirname = "static/images/"
    model = "a_b_pu_model_v1"
    checklist = []
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    for ur in fh:
        url = ur.strip()
        filename = url.split("/")[-1]
        print "downloading %s" % (url)
        img = returnDownloadImageCV2(url)
        aurl = 'http://104.199.154.201:5000/api/maria?url='+str(url)
        r = urllib2.urlopen(aurl)
        jsonData = json.loads(r.read())
        r.close()
        #jdump = json.dumps(jsonData, sort_keys=True, indent=4)
        if 'message' not in jsonData:
            count = 0
            prob = []
            for list in jsonData['detect']:
                cv2.rectangle(img,(list['right'],list['top']),(list['left'],list['bottom']),(0,255,0),3)
                cv2.putText(img,list['class'],(list['left'],list['top']-10),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 0, 255),2)
                count+=1
                prob.append(list['prob'])
            if prob:
                mx = max(prob)
            else:
                mx = 0
            jsonData['prob_max'] = mx
            jsonData['breast_count'] = count
            jdump = json.dumps(jsonData, sort_keys=True, indent=4)
            detectimage = "detect-"+filename
            predict_url = os.path.join(dirname, detectimage)
            cv2.imwrite(predict_url.strip(), img)
            i = ccdb.InsertDB(url, predict_url, jdump, model)
            i.insertData()
            #return os.path.join(dirname, detectimage), json.dumps(jsonData, sort_keys=True, indent=4), url
            checklist.append([os.path.join(dirname, detectimage), json.dumps(jsonData, sort_keys=True, indent=4), url])
    if fh:
        fh.close()
    return checklist

if __name__ == "__main__":
    list = goCheck(sys.argv[1])
    #for l in list:
    #    print l
    #for p in ccdb.PredictDb.select():
    #    print p.result, p.input_url, p.predict_url, p.predict_date
