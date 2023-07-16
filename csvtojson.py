import csv 
import json
import time

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            if row['element_type'] == '1':
                row['element_type'] = 'GK'
            elif row['element_type'] == '2':
                row['element_type'] = 'DEF'
            elif row['element_type'] == '3':
                row['element_type'] = 'MID'
            elif row['element_type'] == '4':
                row['element_type'] = 'FWD'

            new_row = {
                'id': row['id'],
                'first_name': row['first_name'],
                'second_name': row['second_name'],
                'position': row['element_type'],
                'goals_scored': row['goals_scored'],
                'assists': row['assists'],
                'total_points': row['total_points'],
                'minutes': row['minutes'],
                'goals_conceded': row['goals_conceded'],
                'creativity': row['creativity'],
                'influence': row['influence'],
                'threat': row['threat'],
                'bonus': row['bonus'],
                'bps': row['bps'],
                'ict_index': row['ict_index'],
                'clean_sheets': row['clean_sheets'],
                'red_cards': row['red_cards'],
                'yellow_cards': row['yellow_cards'],
                'selected_by_percent': row['selected_by_percent'],
            }
            jsonArray.append(new_row)


    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
        
csvFilePath = r'2016-17\\players_raw.csv'
jsonFilePath = r'data.json'
csv_to_json(csvFilePath, jsonFilePath)