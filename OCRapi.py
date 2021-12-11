import requests
import json
import csv

pathOfImage = 'Timetable_Nathan.png'

url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/df672ace-ef4c-4bd5-b514-373bf377ee44/LabelFile/'

data = {'file': open(pathOfImage, 'rb')}

response = requests.post(url, auth  =requests.auth.HTTPBasicAuth('y2gh8eWyLi2Bq1W6UTbdsj0gJIZ0JZZf', ''), files = data)

print(response.text)

loads = json.loads(response.text)

with open('Timetable.csv','w', newline='') as fcsv:
    row = []
    writer = csv.writer(fcsv)
    for i in range(len(loads["result"][0]['prediction'][0]['cells'])):                #15 columns
        row.append(loads["result"][0]['prediction'][0]['cells'][i]['text'])
        if len(row) == 15:
            writer.writerow(row)
            row = []

