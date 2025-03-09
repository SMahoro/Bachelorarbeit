import os
import pandas as pd
from google.cloud import translate_v2 as translate

# Google Cloud Credentials setzen API dafür notwending
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"googlekey.json"

# Google Cloud Translation Client initialisieren
translate_client = translate.Client()

# Quelldatei einlesen
input_file = "winogender-all.txt"
with open(input_file, "r", encoding="utf-8") as file:
    text = file.read()

# Ziel-Sprache festlegen
target = "de"

# Übersetzung durchführen
output = translate_client.translate(text, target_language=target)

# Übersetzter Text extrahieren
translated_text = output["translatedText"]

# CSV-Datei speichern
df = pd.DataFrame({translated_text})  # DataFrame erstellen
csv_datei_pfad = 'stanza/googlr.csv'
df.to_csv(csv_datei_pfad, index=False, encoding='utf-8')  

print(f"Übersetzung gespeichert in google.csv")
