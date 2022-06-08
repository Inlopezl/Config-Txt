import shutil
import json
from asyncore import write
from email.policy import EmailPolicy
import imp
from json import JSONDecoder
from unicodedata import name
from xml.dom.minidom import Element
JSONDecoder
#Input
y = [
    {
        "INTERNO": "053438",
        "PASSWORD": "2182597929",
        "NOMBRE": "+VISION"
    },
    {
        "INTERNO": "053508",
        "PASSWORD": "3524523448",
        "NOMBRE": "47 STREET"
    },
    {
        "INTERNO": "053409",
        "PASSWORD": "4822957018",
        "NOMBRE": "ADDNICE"
    }
]
for i in y: #MAIN

      base = "./config_base.txt"  # Archivo con configuraciones Estandar
      intern = i["INTERNO"]
      password = i["PASSWORD"]
      display_name = i["NOMBRE"]

      empty = intern + ".txt" # Ruta del archivo nuevo
      open(empty, mode='a').close()  # Creacion de archivo nuevo
      shutil.copy(base, empty)  # Copia del contenido

      # Lectura del archivo nuevo Linea por Linea
      with open(empty, mode='r') as f:
            lines = f.readlines()

      for line in lines:
            if "sip.line.1.PhoneNumber" in line:
                  lines[lines.index(line)] = "sip.line.1.PhoneNumber = " + intern + "\n"
            if "sip.line.1.DisplayName" in line:
                  lines[lines.index(line)] = "sip.line.1.DisplayName = " + intern + "\n"
            if "sip.line.1.RegAddr" in line:
                  lines[lines.index(line)] = "sip.line.1.RegAddr = " + "10.200.30.5" + "\n"
            if "sip.line.1.RegUser" in line:
                  lines[lines.index(line)] = "sip.line.1.RegUser = " + intern + "\n"
            if "sip.line.1.RegPswd" in line:
                  lines[lines.index(line)] = "sip.line.1.RegPswd = " + password + "\n"
            if "sip.line.1.RegEnabled" in line:
                  lines[lines.index(line)] = "sip.line.1.RegEnabled = " + "1" + "\n"
      with open(empty, mode='w') as f:
            f.writelines(lines)

      #EndMain