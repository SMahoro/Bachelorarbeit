import pandas as pd
import os
from dotenv import load_dotenv
import requests, uuid, json


# .env Datei laden
load_dotenv()

# Azure Translator API-Schlüssel
key = os.getenv("api_key")
endpoint = "https://api.cognitive.microsofttranslator.com"

# Einlesen .txt
with open("winogender-all-split2.txt", "r", encoding="utf-8") as file:
    text = file.read()

location = "westeurope"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['de']
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text': text
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

# Speichern in microsoft.csv

df = pd.DataFrame({response})  # DataFrame erstellen
csv_datei_pfad = 'stanza/microsoft.csv'
df.to_csv(csv_datei_pfad, index=False, encoding='utf-8')  
print("Übersetzung gespeichert in CSV")

print("Übersetzung erfolgreich gespeichert in micorsoft.csv")