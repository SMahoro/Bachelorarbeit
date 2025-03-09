import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


print("Start")
# WebDriver initialisieren
driver = webdriver.Firefox()

try:
    # 1. Bing-translate-Seite öffnen
    driver.get('https://www.bing.com/translator?cc=de')
    print("Webseite geoeffnet.")
    driver.find_element("xpath",'//*[@id="tta_input_ta"]').click()


    # 2. Englisch -> Deutsch übersetzen
    datei_pfad = 'berufe.txt'  # Pfad zur Textdatei
   
    
    with open(datei_pfad, 'r', encoding='utf-8') as file:
        text = file.read().strip() 

    # 3. Eingabefeld finden und das Wort aus der Umgebungsvariable 'VOC' eingeben
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="tta_input_ta"]')))
    search.clear()
    search.send_keys(text)#txt 
    print("Eingabe erfolgreich.")

    #4. Übersetzung speichern
    #german = driver.find_elements(By.CLASS_NAME, "ryNqvb")
    time.sleep(10)
    german_elements = driver.find_elements("xpath", '//*[@id="tta_output_ta"]')
    #german = WebDriverWait(driver, 10).until(
    #    EC.presence_of_element_located((By.XPATH, '//*[@id="tta_output_ta')))
 # Texte sammeln
    translations = [ger.text for ger in german_elements]
    print("Übersetzungen gesammelt:", translations)

    # 5. Übersetzungen in CSV-Datei speichern
    df = pd.DataFrame({"Translation": translations})  # DataFrame erstellen
    csv_datei_pfad = 'output_bing.csv'
    df.to_csv(csv_datei_pfad, index=False, encoding='utf-8')  # CSV speichern
    print(f"Übersetzungen wurden in '{csv_datei_pfad}' gespeichert.")


except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")

finally:
    driver.quit()
    print("Browser geschlossen.")