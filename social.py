import csv
import sys
import json, os


def convert(csv_filename, fieldnames):
    print ("Opening CSV file: ",csv_filename)
    f=open(csv_filename, 'r')
    csv_reader = csv.DictReader(f,fieldnames)
    json_filename = "public/"+csv_filename.split(".")[0]+".json"

    print ("Saving JSON to file: ",json_filename)
    jsonf = open(json_filename,'w') 
    data = json.dumps([r for r in csv_reader])
    jsonf.write('{"data":' + data + '}') 
    f.close()
    jsonf.close()


csvfile = ('nazimboudeffa.csv')
field_names = [
                "site",
                "profile",
                "usage"
            ]

convert(csvfile, field_names)