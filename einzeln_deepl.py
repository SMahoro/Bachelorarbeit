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
    # 1. DeepL-translate-Seite öffnen
    driver.get('https://www.deepl.com/de/translator')
    print("Webseite geoeffnet.")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div/div[2]/div/div[3]/button[1]'))).click()
    #warten > cookies entfernen möglich
    print("Cookies abgelehnt")

    # 2. Englisch -> Deutsch übersetzen
    datei_pfad = 'berufe.txt'  # Pfad zur Textdatei   
    with open(datei_pfad, 'r', encoding='utf-8') as file:
        text = file.readlines() 

    # 3. Eingabefeld finden und das Wort aus der Umgebungsvariable 'VOC' eingeben
    search = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/main/div[2]/nav/div/div[2]/div/div/div[1]/div/div/div/div/div/section/div/div[2]/div[1]/section/div/div[1]/d-textarea/div[1]')))
    search.clear()
    for t in text:
        time.sleep(random.randint(1, 10))
        search.clear()
        search.send_keys(t)#txt 
        print("Eingabe erfolgreich.")

        # 4. Übersetzung auslesen
        time.sleep(10)  # Warten, bis die Übersetzung geladen ist
        german_elements =  driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/main/div[2]/nav/div/div[2]/div/div/div[1]/div/div/div/div/div/section/div/div[2]/div[3]/section/div[1]/d-textarea/div')
        translations = [ger.text for ger in german_elements]
        print("Übersetzungen gesammelt:", translations)
        for translation in translations:
            translations_array.append((translation))     


    # 5. Übersetzungen in CSV-Datei speichern
    df = pd.DataFrame(translations_array, columns=["Übersetzung"])  
    csv_datei_pfad = 'stanza/output_einzeln_deepl.csv'
    df.to_csv(csv_datei_pfad, index=False, encoding='utf-8')  # CSV speichern
    print(f"Übersetzungen wurden in '{csv_datei_pfad}' gespeichert.")

except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")

finally:
    # Browser schließen
    driver.quit()
    print("Browser geschlossen.")