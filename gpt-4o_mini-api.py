from openai import OpenAI
from dotenv import load_dotenv
import os
import pandas as pd

# .env Datei laden
load_dotenv()

# API-Key aus der Umgebungsvariable abrufen
api_key = os.getenv("OPENAI_API_KEY")

# OpenAI Client mit API-Key erstellen
client = OpenAI(api_key=api_key)

#Datei einlesen
with open("winogender-all-split1.txt", "r", encoding="utf-8") as file:
    text = file.read().strip()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a translator. Translate text into german"},
        {"role": "user","content": text
    }])
print("Anfrage erfolgreich.")

# Übersetzung extrahieren
übersetzung = completion.choices[0].message.content
# Übersetzung in CSV speichern

df = pd.DataFrame({übersetzung})  # DataFrame erstellen
csv_datei_pfad = 'stanza/gpt-4o_mini-1.csv'
df.to_csv(csv_datei_pfad, index=False, encoding='utf-8')  
print("Übersetzung gespeichert in gpt-40-mini.CSV")

