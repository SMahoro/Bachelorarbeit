import deepl
import pandas as pd
import os
from dotenv import load_dotenv


# .env Datei laden
load_dotenv()

# DeepL API-Schlüssel
auth_key = os.getenv("auth_key")
translator = deepl.Translator(auth_key)

# Einlesen von .txt
with open("winogender_all.csv", "r", encoding="utf-8") as file:
    text = file.read()

# Übersetzen
translated_text = translator.translate_text(text, target_lang="DE").text

# Speichern in deepl.csv

df = pd.DataFrame({translated_text})  # DataFrame erstellen
csv_datei_pfad = 'stanza/deepl.csv'
df.to_csv(csv_datei_pfad, index=False, encoding='utf-8')  

print("Übersetzung erfolgreich gespeichert in deepl.csv")
