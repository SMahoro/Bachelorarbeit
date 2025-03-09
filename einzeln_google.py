import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random



print("Start")
# WebDriver initialisieren
driver = webdriver.Firefox()
translations_array = []


try:
    # 1. Google-translate-Seite öffnen
    driver.get('https://translate.google.de/')
    print("Webseite geoeffnet.")
    driver.find_element("xpath",'/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div/div/button/span[6]').click()


    # 2. Englisch -> Deutsch übersetzen
    datei_pfad = 'berufe.txt'  # Pfad zur Textdatei   
    with open(datei_pfad, 'r', encoding='utf-8') as file:
        text = file.readlines()

    # 3. Eingabefeld finden und das Wort aus der Umgebungsvariable 'VOC' eingeben
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/div/c-wiz/span/span/div/textarea')))
    search.clear()
    for t in text:
        time.sleep(random.randint(1, 10))
        search.clear()
        search.send_keys(t)#txt 
        print("Eingabe erfolgreich.")

        # 4. Übersetzung auslesen
        time.sleep(5)  # Warten, bis die Übersetzung geladen ist
        german_elements = driver.find_elements(By.XPATH, '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz/div[1]/div[7]')
        translations = [ger.text for ger in german_elements]
        print("Übersetzungen gesammelt:", translations)
        for translation in translations:
            translations_array.append((translation))         
       
    # Texte sammeln
    translations = [ger.text for ger in german_elements]
    print("Übersetzungen gesammelt:", translations)

    # 5. Übersetzungen in CSV-Datei speichern
    df = pd.DataFrame(translations_array, columns=["Übersetzung"])  
# CSV speichern
    csv_datei_pfad = 'stanza/output_einzeln_google.csv'
    df.to_csv(csv_datei_pfad, index=False, encoding='utf-8') 
    print(f"Übersetzungen wurden in '{csv_datei_pfad}' gespeichert.")

except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")

finally:
    # Browser schließen
    driver.quit()
    print("Browser geschlossen.")