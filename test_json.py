# Write your awesome code here
import json
import re
import unittest


def check(data):
    erros = {"errors": 0, "bus_id": 0, "stop_id": 0, "stop_name": 0, "next_stop": 0, "stop_type": 0, "a_time": 0}

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
            if x != "" and not x[0].isupper() and (x.lower().find("Road") != -1 or x.lower().find("Avenue")!=-1 or x.lower().find("Boluevard")!=-1 or x.lower().find("Str")!=-1):
                erros['stop_name'] += 1
                erros['errors'] += 1
            elif x == '':
                erros['stop_name'] += 1
                erros['errors'] += 1
        else:
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
            if ":" not in i['a_time'] and len(i['a_time']) != 5:
                erros['a_time'] += 1
                erros['errors'] += 1

    # print("Type and required field validation:", erros['errors'])
    # print("bus_id:", erros['bus_id'])
    # print("stop_id:", erros['stop_id'])
    # print("stop_name:", erros['stop_name'])
    # print("next_stop:", erros['next_stop'])
    # print("stop_type:", erros['stop_type'])
    # print("a_time:", erros['a_time'])
    print(erros)
    print("-" * 15)

    return erros

# d = input()
# d = json.loads(d)
a = [{"bus_id":128,"stop_id":1,"stop_name":"Prospekt Avenue","next_stop":3,"stop_type":"S","a_time":8.12},{"bus_id":128,"stop_id":3,"stop_name":"","next_stop":5,"stop_type":"","a_time":"08:19"},{"bus_id":128,"stop_id":5,"stop_name":"Fifth Avenue","next_stop":7,"stop_type":"O","a_time":"08:25"},{"bus_id":128,"stop_id":"7","stop_name":"Sesame Street","next_stop":0,"stop_type":"F","a_time":"08:37"},{"bus_id":"","stop_id":2,"stop_name":"Pilotow Street","next_stop":3,"stop_type":"S","a_time":""},{"bus_id":256,"stop_id":3,"stop_name":"Elm Street","next_stop":6,"stop_type":"","a_time":"09:45"},{"bus_id":256,"stop_id":6,"stop_name":"Sunset Boulevard","next_stop":7,"stop_type":"","a_time":"09:59"},{"bus_id":256,"stop_id":7,"stop_name":"Sesame Street","next_stop":"0","stop_type":"F","a_time":"10:12"},{"bus_id":512,"stop_id":4,"stop_name":"Bourbon Street","next_stop":6,"stop_type":"S","a_time":"08:13"},{"bus_id":"512","stop_id":6,"stop_name":"Sunset Boulevard","next_stop":0,"stop_type":5,"a_time":"08:16"}]
b = [{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Fifth Avenue", "next_stop" : 4, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 4, "stop_name" : "Abbey Road", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"},  {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Santa Monica Boulevard", "next_stop" : 8, "stop_type" : "O", "a_time" : "08:25"},  {"bus_id" : 128, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 11, "stop_type" : "", "a_time" : "08:37"},  {"bus_id" : 128, "stop_id" : 11, "stop_name" : "Beale Street", "next_stop" : 12, "stop_type" : "", "a_time" : "09:20"},  {"bus_id" : 128, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 14, "stop_type" : "", "a_time" : "09:45"},  {"bus_id" : 128, "stop_id" : 14, "stop_name" : "Bourbon Street", "next_stop" : 19, "stop_type" : "O", "a_time" : "09:59"},  {"bus_id" : 128, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"},  {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:13"},  {"bus_id" : 256, "stop_id" : 3, "stop_name" : "Startowa Street", "next_stop" : 8, "stop_type" : "", "a_time" : "08:16"},  {"bus_id" : 256, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 10, "stop_type" : "", "a_time" : "08:29"},  {"bus_id" : 256, "stop_id" : 10, "stop_name" : "Lombard Street", "next_stop" : 12, "stop_type" : "", "a_time" : "08:44"},  {"bus_id" : 256, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 13, "stop_type" : "O", "a_time" : "08:46"},  {"bus_id" : 256, "stop_id" : 13, "stop_name" : "Orchard Road", "next_stop" : 16, "stop_type" : "", "a_time" : "09:13"},  {"bus_id" : 256, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 17, "stop_type" : "O", "a_time" : "09:26"},  {"bus_id" : 256, "stop_id" : 17, "stop_name" : "Khao San Road", "next_stop" : 20, "stop_type" : "O", "a_time" : "10:25"},  {"bus_id" : 256, "stop_id" : 20, "stop_name" : "Michigan Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "11:26"},  {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Arlington Road", "next_stop" : 7, "stop_type" : "S", "a_time" : "11:06"},  {"bus_id" : 512, "stop_id" : 7, "stop_name" : "Parizska Street", "next_stop" : 8, "stop_type" : "", "a_time" : "11:15"},  {"bus_id" : 512, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 9, "stop_type" : "", "a_time" : "11:56"},  {"bus_id" : 512, "stop_id" : 9, "stop_name" : "Niebajka Avenue", "next_stop" : 15, "stop_type" : "", "a_time" : "12:20"},  {"bus_id" : 512, "stop_id" : 15, "stop_name" : "Jakis Street", "next_stop" : 16, "stop_type" : "", "a_time" : "12:44"},  {"bus_id" : 512, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 18, "stop_type" : "", "a_time" : "13:01"},  {"bus_id" : 512, "stop_id" : 18, "stop_name" : "Jakas Avenue", "next_stop" : 19, "stop_type" : "", "a_time" : "14:00"},  {"bus_id" : 1024, "stop_id" : 21, "stop_name" : "Karlikowska Avenue", "next_stop" : 12, "stop_type" : "S", "a_time" : "13:01"},  {"bus_id" : 1024, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:00"},  {"bus_id" : 512, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:11"}]
c = [{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Fifth Avenue", "next_stop" : 4, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 4, "stop_name" : "abbey Road", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"},  {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Santa Monica Boulevard", "next_stop" : 8, "stop_type" : "O", "a_time" : "08:25"},  {"bus_id" : 128, "stop_id" : 8, "stop_name" : "Elm Street Str.", "next_stop" : "11", "stop_type" : "", "a_time" : "08:37"},  {"bus_id" : 128, "stop_id" : 11, "stop_name" : "Beale Street", "next_stop" : 12, "stop_type" : "", "a_time" : "09:20"},  {"bus_id" : 128, "stop_id" : 12, "stop_name" : 9, "next_stop" : 14, "stop_type" : "", "a_time" : "09:45"},  {"bus_id" : 128, "stop_id" : "five", "stop_name" : "Bourbon street", "next_stop" : 19, "stop_type" : "O", "a_time" : "09:59"},  {"bus_id" : 128, "stop_id" : 19, "stop_name" : "", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"},  {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:13"},  {"bus_id" : "", "stop_id" : "", "stop_name" : "Startowa Street", "next_stop" : 8, "stop_type" : 23.9, "a_time" : 8},  {"bus_id" : 256, "stop_id" : 8, "stop_name" : "Elm", "next_stop" : 10, "stop_type" : "", "a_time" : "08:29"},  {"bus_id" : 256, "stop_id" : 10, "stop_name" : "Lombard Street", "next_stop" : 12, "stop_type" : "", "a_time" : "08:44"},  {"bus_id" : 256, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : "", "stop_type" : "O", "a_time" : "08:46"},  {"bus_id" : 256, "stop_id" : 13, "stop_name" : 34.6, "next_stop" : 16, "stop_type" : "", "a_time" : "09:13"},  {"bus_id" : "eleven", "stop_id" : 16, "stop_name" : "Sunset Boullevard", "next_stop" : 17.4, "stop_type" : "O", "a_time" : "09:26"},  {"bus_id" : 256, "stop_id" : 17, "stop_name" : "Khao San Road", "next_stop" : 20, "stop_type" : "O", "a_time" : "10:25"},  {"bus_id" : 256, "stop_id" : 20, "stop_name" : "Michigan Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "11:26"},  {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Arlington Road", "next_stop" : 7, "stop_type" : "S", "a_time" : "11:06"},  {"bus_id" : 512, "stop_id" : 7, "stop_name" : "Parizska St.", "next_stop" : 8, "stop_type" : "", "a_time" : "11:15"},  {"bus_id" : 512, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 9, "stop_type" : "", "a_time" : "11:56"},  {"bus_id" : 512, "stop_id" : 9, "stop_name" : "Niebajka Av.", "next_stop" : 15, "stop_type" : "", "a_time" : "12:20"},  {"bus_id" : 512, "stop_id" : 15, "stop_name" : "Jakis Street", "next_stop" : 16, "stop_type" : "", "a_time" : "12:44"},  {"bus_id" : 512, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 18, "stop_type" : "", "a_time" : "13:01"},  {"bus_id" : 512, "stop_id" : 18, "stop_name" : "Jakas Avenue", "next_stop" : 19, "stop_type" : 3, "a_time" : "14:00"},  {"bus_id" : 1024, "stop_id" : "21", "stop_name" : "Karlikowska Avenue", "next_stop" : 12, "stop_type" : "S", "a_time" : 13.01},  {"bus_id" : 1024, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "FF", "a_time" : ""},  {"bus_id" : "", "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:11"}]

# check(b)

class Test_main(unittest.TestCase):

    def test_check(self):
        self.assertEqual(check(a), {"errors": 8, "bus_id": 2, "stop_id": 1, "stop_name": 1, "next_stop": 1, "stop_type": 1, "a_time": 2})
        self.assertEqual(check(b), {"errors": 0, "bus_id": 0, "stop_id": 0, "stop_name": 0, "next_stop": 0, "stop_type": 0, "a_time": 0})
        self.assertEqual(check(c), {"errors": 18, "bus_id": 3, "stop_id": 3, "stop_name": 3, "next_stop": 3, "stop_type": 3, "a_time": 3})
        
# py -3.9 -m unittest main.py
