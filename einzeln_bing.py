import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time


print("Start")
driver = webdriver.Firefox()
translations_array = []

try:
    # 1. Bing-translate-Seite öffnen
    driver.get('https://www.bing.com/translator?cc=de')
    print("Webseite geoeffnet.")
    driver.find_element("xpath",'//*[@id="tta_input_ta"]').click()

    # 2. Englisch -> Deutsch übersetzen
    datei_pfad = 'berufe.txt'  
    with open(datei_pfad, 'r', encoding='utf-8') as file:
        text = file.readlines() 

    # 3. Eingabefeld finden und das Wort aus der Umgebungsvariable '.txt' eingeben
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="tta_input_ta"]')))
    search.clear()
    for t in text:
        time.sleep(random.randint(1, 10))
        search.clear()
        search.send_keys(t)#txt 
        print("Eingabe erfolgreich.")

        #4. Übersetzung speichern
        time.sleep(5)
        german_elements = driver.find_elements("xpath", '//*[@id="tta_output_ta"]')
        translations = [ger.text for ger in german_elements]
        print("Übersetzungen gesammelt:", translations)
        for translation in translations:
            translations_array.append((translation))         

# 5. Übersetzungen in CSV-Datei speichern
    df = pd.DataFrame(translations_array, columns=["Übersetzung"])  
    csv_datei_pfad = 'stanza/output_einzeln_bing.csv'
    df.to_csv(csv_datei_pfad, index=False, encoding='utf-8')  # CSV speichern
    print(f"Übersetzungen wurden in '{csv_datei_pfad}' gespeichert.")


except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")

finally:
    driver.quit()
    print("Browser geschlossen.")