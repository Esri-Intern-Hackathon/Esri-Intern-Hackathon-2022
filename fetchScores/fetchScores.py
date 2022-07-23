import requests
import csv
import json


listOfRows = []
def callApi(lat, lon):
    scoreUrl = "https://api.walkscore.com/score"
    params = \
        {
         'format': 'json',
         'lat': lat,
         'lon': lon,
         'transit': 1,
         'bike': 1,
         'wsapikey':"693ebce29aab8effc392c534256ab612"
         }

    r = requests.get(scoreUrl, params=params)
    return r

def readZipCodeCSV(input_file):
    with open(input_file, 'r') as read_obj:
        csv_reader = csv.reader(read_obj, delimiter=',')
        line_count = 0
        for row in csv_reader:
            listOfRows.append([row[0], row[1], row[2]])

def readFromScoreFile(inputTxtFile):
    file1 = open(inputTxtFile,"r")
    print(file1.read()) 

if __name__=='__main__':
    readZipCodeCSV('zip-code-lat-lon.csv')

    # readFromScoreFile("scoresFile.txt")

    listOfRows[0].append("Walk Score")
    listOfRows[0].append("Walk Description")
    listOfRows[0].append("Transit Score")
    listOfRows[0].append("Transit Description")
    listOfRows[0].append("Bike Score")
    listOfRows[0].append("Bike Description")
    # print(listOfRows[1])

    scoresListOfList = [[]]

    for i in range(1, len(listOfRows)):
        lat = listOfRows[i][1]
        lon = listOfRows[i][2]
        print(lat, lon)
        scores = callApi(lat, lon)
        scoresJsonStr = scores.text
        json_object = json.loads(scoresJsonStr)
        # print(json_object)
        
        scoresListOfList.append([json_object["walkscore"], json_object["description"], json_object["transit"]["score"], \
        json_object["transit"]["description"], json_object["bike"]["score"], json_object["bike"]["description"]])

    # print(scoresListOfList)
    for i in range(1, len(listOfRows)):
        for j in range(6):
            listOfRows[i].append(scoresListOfList[i][j])
    
    # print(listOfRows[:3])

    file = open('output.csv', 'w+', newline ='')
 
    # writing the data into the file
    with file:   
        write = csv.writer(file)
        write.writerows(listOfRows)


    # print(scoresListOfList)
    # print(zipCodesNotThereList)

    # strToWrite = str(scoresListOfList)

    # file1 = open("scoresFile.txt","w")
    # file1.write(strToWrite)


    