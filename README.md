# Gender Bias - Bachelorarbeit

## Über das Projekt
Dieses Projekt wurde im Rahmen einer Bachelorarbeit an der **HTW Berlin** implementiert. Ziel ist es, den **Gender Bias** in verschiedenen **Übersetzungstools** (Microsoft/Bing, Google, DeepL und ChatGPT) zu analysieren. Dabei wurden unter anderem die Datensätze von **Winogender** sowie die Anwendung **Stanza** genutzt.

Die Ergebnisse und extrahierten Übersetzungen befinden sich in den Ordnern:
- **stanza**
- **Datensatz**

---

## Voraussetzungen
Um die Anwendung zu nutzen, wird benötigt:
- Einen **API-Schlüssel** für die genannten Übersetzungsdienste (nur für Extraktion & Analyse der Sätze notwendig, **außer bei GPT-4o mini**).
- Installierte **Jupyter Notebook**-Umgebung und die **Programmiersprache Python**.

---

## Installation

### 1. Paket herunterladen

### 2. Abhängigkeiten installieren

#### Im Ordner `Gender Bias - Bachelorarbeit`
```bash
pip install -r requirements.txt
```

#### Im Ordner `Stanza`
```bash
conda install -c stanfordnlp stanza
```

---

## Scrapen
Das Scraping erfolgt im Ordner `Gender Bias - Bachelorarbeit`. 
- Nach dem Starten des Programms werden die neuen Übersetzungen automatisch in den Zielordnern **überschrieben**.
- In einigen Fällen kann es notwendig sein, die extrahierten Daten **manuell zu bearbeiten**, bevor sie zur Analyse genutzt werden können.

---

## Auswertung
Die Analyse erfolgt im Ordner `stanza`:
- Dateien mit dem Namen **`Auswertung.ipynb`** führen die **Analyse** durch.
- Dateien mit dem Namen **`Graphen.ipynb`** enthalten die **visualisierten Ergebnisse**.

---

## Zitation

### **Stanza**
```bibtex
@inproceedings{bauer-etal-2023-semgrex,
    title = "Semgrex and Ssurgeon, Searching and Manipulating Dependency Graphs",
    author = "Bauer, John  and
      Kiddon, Chlo{\'e}  and
      Yeh, Eric  and
      Shan, Alex  and
      D. Manning, Christopher",
    booktitle = "Proceedings of the 21st International Workshop on Treebanks and Linguistic Theories (TLT, GURT/SyntaxFest 2023)",
    month = mar,
    year = "2023",
    address = "Washington, D.C.",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.tlt-1.7",
    pages = "67--73"
}
```

### **Winogender-Schemas**
```bibtex
@InProceedings{rudinger-EtAl:2018:N18,
  author    = {Rudinger, Rachel  and  Naradowsky, Jason  and  Leonard, Brian  and  {Van Durme}, Benjamin},
  title     = {Gender Bias in Coreference Resolution},
  booktitle = {Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
  month     = {June},
  year      = {2018},
  address   = {New Orleans, Louisiana},
  publisher = {Association for Computational Linguistics}
}
```

---
# Gender-Bias---Bachelorarbeit
