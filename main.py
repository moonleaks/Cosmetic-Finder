
import requests
import os
import json
import time



cosmeticname = input("Name: ")

r = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?name={cosmeticname}')
data = r.json()
print(data)
out_file = open("cosmeticsid.json", "w")
json.dump(data, out_file, indent = 4)
out_file.close()
name = data["data"]["name"]
icon = data["data"]["images"]["icon"]
description = data["data"]["description"]
value = data["data"]["rarity"]["value"]
set = data["data"]["set"]["value"]
path = data["data"]["path"]
type = data["data"]["type"]["value"]
id = data["data"]["id"]



print('    ')
print('    ')
print('    ')
print("Cosmetic's Info")
print("-------------------")
print(f'Name: {name}')
print(f'Icon: {icon}')
print(f'Description: {description}')
print(f'Value: {value}')
if set == None:
      print("Set: Null")
else:
  print(f'Set: {set}')
print(f'path: {path}')
print(f'Type: {type}')
print(f'ID: {id}')

time.sleep(int(100))

out_file.close()