import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time



print("Start")
driver = webdriver.Firefox()

try:
    # 1. DeepL-translate-Seite öffnen
    driver.get('https://www.deepl.com/de/translator')
    print("Webseite geoeffnet.")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div/div[2]/div/div[3]/button[1]'))).click()
    print("Cookies abgelehnt")


    # 2. Datei
    datei_pfad = 'berufe.txt'  # Pfad zur Textdatei 
    with open(datei_pfad, 'r', encoding='utf-8') as file:
        text = file.read().strip() 

    # 3. Eingabefeld finden und das Wort aus der Umgebungsvariable 'VOC' eingeben
    search = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/main/div[2]/nav/div/div[2]/div/div/div[1]/div/div/div/div/div/section/div/div[2]/div[1]/section/div/div[1]/d-textarea/div[1]')))

    search.clear()
    search.send_keys(text)#txt 
    print("Eingabe erfolgreich.")

    #4. Übersetzung speichern
    time.sleep(10)
    german_elements =  driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/main/div[2]/nav/div/div[2]/div/div/div[1]/div/div/div/div/div/section/div/div[2]/div[3]/section/div[1]/d-textarea/div')

    translations = [ger.text for ger in german_elements]
    print("Übersetzungen gesammelt:", translations)

    # 5. Übersetzungen in CSV-Datei speichern
    df = pd.DataFrame({"Translation": translations})  # DataFrame erstellen
    csv_datei_pfad = 'stanza/output_deepl.csv'
    df.to_csv(csv_datei_pfad, index=False, encoding='utf-8')  # CSV speichern
    print(f"Übersetzungen wurden in '{csv_datei_pfad}' gespeichert.")


except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")

finally:
    driver.quit()
    print("Browser geschlossen.")