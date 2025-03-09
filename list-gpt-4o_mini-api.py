from openai import OpenAI
from dotenv import load_dotenv
import os
import csv

# .env Datei laden
load_dotenv()

# API-Key aus der Umgebungsvariable abrufen
api_key = os.getenv("OPENAI_API_KEY")

# OpenAI Client mit API-Key erstellen
client = OpenAI(api_key=api_key)

#Datei einlesen
with open("berufe.txt", "r", encoding="utf-8") as file:
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
with open("stanza/output-gpt-4o_mini-2.csv", "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([übersetzung])

print("Übersetzung gespeichert in CSV")

