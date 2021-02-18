# Write your awesome code here
import json
import re
import unittest
from collections import Counter

def check(data):
    erros = {"errors": 0, "bus_id": 0, "stop_id": 0, "stop_name": 0, "next_stop": 0, "stop_type": 0, "a_time": 0}
    sn= []
    for i in data:
        # bus_id <int> 128, 256, 512, Req
        if (isinstance(i['bus_id'], int) and i['bus_id'] not in [128, 256, 512, 1024]) or not isinstance(i['bus_id'], int):
            erros['bus_id'] += 1
            erros['errors'] += 1
        # stop_id <int>, Req
        if not isinstance(i['stop_id'], int):
            erros['stop_id'] += 1
            erros['errors'] += 1
        # stop_name <str>, Req, include ["Road", "Avenue", "Boulevard", "Street"], is upper
        x = i['stop_name']
        if isinstance(x, str):
            regexp = "(^([A-Z]\w+) ?\w* (Avenue|Road|Boulevard|Street)$)"
            res = re.findall(regexp, x)
            if len(res) == 0:
                erros['stop_name'] += 1
                erros['errors'] += 1
                sn.append(x)
        else:
            sn.append(x)
            erros['stop_name'] += 1
            erros['errors'] += 1
        # next_stop <int>, Req
        if not isinstance(i['next_stop'], int) or i['next_stop'] is None:
            erros['next_stop'] += 1
            erros['errors'] += 1
        # stop_type <char>, ['S', 'O', 'F']
        if isinstance(i['stop_type'], str) and i['stop_type'] not in ['S', 'O', 'F', ''] or not isinstance(i['stop_type'], str):
            erros['stop_type'] += 1
            erros['errors'] += 1
        # a_time <str>, 5char, HH:MM, Req
        if not isinstance(i['a_time'], str):
            erros['a_time'] += 1
            erros['errors'] += 1
        else:
            regexp = "^[.0-2]\d:[0-5]\d$"
            res = re.findall( regexp, i['a_time'])
            if len(res) == 0:
                erros['a_time'] += 1
                erros['errors'] += 1
    print("Format validation: {} errors:".format(erros['errors']))
    print("stop_name:", erros['stop_name'])
    print("stop_type:", erros['stop_type'])
    print("a_time:", erros['a_time'])
    print("-" * 15)
    print(sn)
    return erros

def search_bus(data):
    buses = []
    stops = {}
    for i in data:
        if i['bus_id'] not in stops:
            stops[i['bus_id']] = []
            stops[i['bus_id']].append(i['stop_id'])
        else:
            stops[i['bus_id']].append(i['stop_id'])
    # print("Line names and number of stops:")
    # for key, value in stops.items():
        # print(f"bus_id: {key}, stops: {len(value)}")
    return stops

def check_line(data, buses):
    b = {}
    s, f, t = [], [], []
    test = {}
    for key in buses.keys():
        b[key]=[]
        for i in data:
            test.setdefault(i['stop_name'], [])
            test[i['stop_name']].append(key)
            if i['bus_id'] == key:
                if i['stop_type'] == "S":
                    b[key].append(i['stop_type'])
                    s.append(i['stop_name'])   
                elif i['stop_type'] =="F":
                    b[key].append(i['stop_type'])    
                    f.append(i['stop_name'])  
    
    for key, value in test.items():
        for _ in list(set(value)):
            if value.count(_) > 1:
                t.append(key)
                 
    for key, value in b.items():
        if not value.count("S") == value.count("F"):
            
            print(f"There is no start or end stop for the line: {key}")
            return f"There is no start or end stop for the line: {key}"
    s = list(set(s))
    t = list(set(t))
    f = list(set(f))
    print()
    print(f"Start stops: {len(s)} {sorted(s)}")
    print(f"Transfer stops: {len(t)} {sorted(t)}")
    print(f"Finish stops: {len(f)} {sorted(f)}")
    
def arrival_times(data, stops):
    lines =list(stops.keys())
    lines = {key: [] for key in lines}
    print(lines)
    print()
    worng_line = {}
    
    for line in lines:
        b_time = None
        for i in data: 
            if i['bus_id'] == line:
                if b_time == None:
                    b_time = time.strptime(i['a_time'], "%H:%M")
                else:
                    a_time = time.strptime(i['a_time'], "%H:%M")
                    if b_time >= a_time:
                        # print(time.strftime("%H:%M", b_time) , ">=", time.strftime("%H:%M", a_time), i['stop_name'])
                        worng_line[line] = i['stop_name']
                        break
                    else:
                        b_time = a_time
                        
                # lines[line].append((i['a_time']))
    print(len(worng_line.values()))
    if len(worng_line.values()) > 0:
        print("Arrival time test:")
        for key, value in worng_line.items():
            if value != None:
                print(f"bus_id line {key}: wrong time on station {value}")
    else:
        print("OK")

def on_demand(data):
    wrong = []
    wrong1 = {}

    for stop in data:
        if stop['stop_name'] not in wrong1:
            wrong1[stop['stop_name']] = []
            wrong1[stop['stop_name']].append(stop['stop_type'])
        else:
            wrong1[stop['stop_name']].append(stop['stop_type'])
    for a, b in wrong1.items():
        if "F" in b and "O" in b:
            wrong.append(a)
        if "" in b and "O" in b:
            wrong.append(a)

    wrong = list(set(wrong))
    print("On demand stops test:")
    if len(wrong) > 0:
        print("Wrong stop type:", wrong)
    else:
        print("OK")

t6_1 = [{"bus_id":128,"stop_id":1,"stop_name":"Prospekt Avenue","next_stop":3,"stop_type":"S","a_time":"08:12"},{"bus_id":128,"stop_id":3,"stop_name":"Elm Street","next_stop":5,"stop_type":"O","a_time":"08:19"},{"bus_id":128,"stop_id":5,"stop_name":"Fifth Avenue","next_stop":7,"stop_type":"O","a_time":"08:25"},{"bus_id":128,"stop_id":7,"stop_name":"Sesame Street","next_stop":0,"stop_type":"F","a_time":"08:37"},{"bus_id":256,"stop_id":2,"stop_name":"Pilotow Street","next_stop":3,"stop_type":"S","a_time":"09:20"},{"bus_id":256,"stop_id":3,"stop_name":"Elm Street","next_stop":6,"stop_type":"","a_time":"09:45"},{"bus_id":256,"stop_id":6,"stop_name":"Sunset Boulevard","next_stop":7,"stop_type":"O","a_time":"09:59"},{"bus_id":256,"stop_id":7,"stop_name":"Sesame Street","next_stop":0,"stop_type":"F","a_time":"10:12"},{"bus_id":512,"stop_id":4,"stop_name":"Bourbon Street","next_stop":6,"stop_type":"S","a_time":"08:13"},{"bus_id":512,"stop_id":6,"stop_name":"Sunset Boulevard","next_stop":0,"stop_type":"F","a_time":"08:16"}]
t6_2 = [{"bus_id":512,"stop_id":4,"stop_name":"Bourbon Street","next_stop":6,"stop_type":"S","a_time":"08:13"},{"bus_id":512,"stop_id":6,"stop_name":"Sunset Boulevard","next_stop":0,"stop_type":"F","a_time":"08:16"}]
t6_3 = [{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Fifth Avenue", "next_stop" : 4, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 4, "stop_name" : "Abbey Road", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"},  {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Santa Monica Boulevard", "next_stop" : 8, "stop_type" : "O", "a_time" : "08:25"},  {"bus_id" : 128, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 11, "stop_type" : "", "a_time" : "08:37"},  {"bus_id" : 128, "stop_id" : 11, "stop_name" : "Beale Street", "next_stop" : 12, "stop_type" : "", "a_time" : "09:20"},  {"bus_id" : 128, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 14, "stop_type" : "", "a_time" : "09:45"},  {"bus_id" : 128, "stop_id" : 14, "stop_name" : "Bourbon Street", "next_stop" : 19, "stop_type" : "O", "a_time" : "09:59"},  {"bus_id" : 128, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"},  {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:13"},  {"bus_id" : 256, "stop_id" : 3, "stop_name" : "Startowa Street", "next_stop" : 8, "stop_type" : "", "a_time" : "08:16"},  {"bus_id" : 256, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 10, "stop_type" : "", "a_time" : "08:29"},  {"bus_id" : 256, "stop_id" : 10, "stop_name" : "Lombard Street", "next_stop" : 12, "stop_type" : "", "a_time" : "08:44"},  {"bus_id" : 256, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 13, "stop_type" : "O", "a_time" : "08:46"},  {"bus_id" : 256, "stop_id" : 13, "stop_name" : "Orchard Road", "next_stop" : 16, "stop_type" : "", "a_time" : "09:13"},  {"bus_id" : 256, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 17, "stop_type" : "O", "a_time" : "09:26"},  {"bus_id" : 256, "stop_id" : 17, "stop_name" : "Khao San Road", "next_stop" : 20, "stop_type" : "O", "a_time" : "10:25"},  {"bus_id" : 256, "stop_id" : 20, "stop_name" : "Michigan Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "11:26"},  {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Arlington Road", "next_stop" : 7, "stop_type" : "S", "a_time" : "11:06"},  {"bus_id" : 512, "stop_id" : 7, "stop_name" : "Parizska Street", "next_stop" : 8, "stop_type" : "", "a_time" : "11:15"},  {"bus_id" : 512, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 9, "stop_type" : "", "a_time" : "11:56"},  {"bus_id" : 512, "stop_id" : 9, "stop_name" : "Niebajka Avenue", "next_stop" : 15, "stop_type" : "", "a_time" : "12:20"},  {"bus_id" : 512, "stop_id" : 15, "stop_name" : "Jakis Street", "next_stop" : 16, "stop_type" : "", "a_time" : "12:44"},  {"bus_id" : 512, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 18, "stop_type" : "", "a_time" : "13:01"},  {"bus_id" : 512, "stop_id" : 18, "stop_name" : "Jakas Avenue", "next_stop" : 19, "stop_type" : "", "a_time" : "14:00"},  {"bus_id" : 1024, "stop_id" : 21, "stop_name" : "Karlikowska Avenue", "next_stop" : 12, "stop_type" : "S", "a_time" : "13:01"},  {"bus_id" : 1024, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:00"},  {"bus_id" : 512, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:11"}]


on_demand(t6_1)


