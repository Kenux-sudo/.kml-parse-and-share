import sock as sock
from pykml import parser
import pandas as pd
from os import path
from Bluetooth import *
import time


#kml_file = path.join( \
  #  'C:\\Users\\plotn\\Desktop\\pykml-0.2.0\\src\\pykml\\parser.py', \
    #    'http://code.google.com/apis/kml/documentation/KML_samples.kml', \
      #      'C:\\Users\\plotn\\Desktop\\ghhh.kml')
      
kml_file = 'C:\\Users\\plotn\\Desktop\\ghhh.kml'

bd_addr = "98:D3:32:70:9F:9A"
port = 1
sock = BluetoothSocket(RFCOMM)
    
with open(kml_file) as f:
    doc = parser.parse(f).getroot().Document  # тут содержимое kml
    
plnm = []
pllon = []
pllat = []
    
for pm in doc.Placemark:  # тут парсим данные о метке, например название и координаты
    plnm1 = pm.name
    pllon1 = pm.LookAt.longitude
    pllat1 = pm.LookAt.latitude
    
    plnm.append(plnm1.text)
    pllon.append(pllon1.text)
    pllat.append(pllat1.text)

# создаем список со всеми метками
df = pd.DataFrame()
df['name'] = plnm
df['longitude'] = pllon
df['latitude'] = pllat

# передаем список
sock.connect ((bd_addr, port))
sock.send(df)
sock.close