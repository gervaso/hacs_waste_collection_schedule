import requests
import pandas as pd

from datetime import datetime
from io import StringIO

TITLE = "a&t2000 servizi ambientali"
DESCRIPTION = "Source for a&t2000 servizi ambientali."
URL = None
TEST_CASES = {
    "Pavia di Udine": {"town": "pavia-di-udine"},
    "San Daniele del Friuli": {"town": "san-daniele-del-friuli"},
    "Codroipo": {"town": "codroipo"},
    "Sappada": {"town": "sappada"},
    "Mortegliano": {"town": "mortegliano"},
}
ICON_MAP = {
    "SECCO RESIDUO": "mdi:trash-can",
    "VETRO": "mdi:glass-fragile",
    "CARTA E CARTONE": "mdi:newspaper",
    "ORGANICO UMIDO": "mdi:food",
    "IMBALLAGGI IN PLASTICA E LATTINE": "mdi:recycle",
}


r = requests.get('https://aet2000.it/servizi-comune-di-pavia-di-udine/')
df_list = pd.read_html(StringIO(r.text)) # this parses all the tables in webpages to a list
df = df_list[0]

df.columns = df.iloc[0] #use the first row as a header
df = df.drop(df.index[0])

print(df)

class Source:
    def __init__(self, town):
        self._town = town
        self._url = "https://aet2000.it/servizi-" + town
    
    def fetch(self):
        entries = []
        r = requests.get(self._url)
        df_list = pd.read_html(StringIO(r.text)) # this parses all the tables in webpages to a list
        df = df_list[0]

        df.columns = df.iloc[0] #use the first row as a header
        df = df.drop(df.index[0])


        return entries
