# -*- coding: utf-8 -*-

import datetime
import json
import serial
import time
from elasticsearch import Elasticsearch

ser = serial.Serial("/dev/ttyACM3")
ser.flushInput()

es = Elasticsearch(["http://127.0.0.1:9200"], http_auth = ("elastic", "ELK_PASSWORD"))


while True:
    try:
        ser_bytes = ser.readline()
        data = ser_bytes.decode("UTF-8")

        data = data.split(" ")

        if len(data) == 3:
            items = {}
            print("------------------------")
            print("HUMIDITY:\t" + data[0])
            print("TEMPERATURE:\t" + data[1])
            print("GAS:\t\t" + data[2])
            print("------------------------")

            print("Sending to ES...")
            items["humidity"] = float(data[0])
            items["temperature"] = float(data[1])
            items["gas"] = float(data[2])
            items["date"] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

            data = json.dumps(items)
            print(data)
            es.index(index = "dc_monitor_logs", doc_type = "dcmonitor", body = data)
    except:
        pass

    time.sleep(0.1)

ser.close()
