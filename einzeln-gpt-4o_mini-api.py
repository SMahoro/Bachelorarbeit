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

# Datei zeilenweise einlesen und übersetzen
übersetzungen = []
with open("berufe.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if line:  # Leere Zeilen ignorieren
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a translator. Translate text into German"},
                    {"role": "user", "content": line}
                ]
            )
            übersetzung = completion.choices[0].message.content
            übersetzungen.append([übersetzung]) 

# Übersetzungen in CSV speichern
with open("stanza/output_einzeln_gpt-4o_mini-2.csv", "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(übersetzungen)

print("Übersetzungen gespeichert in CSV")
