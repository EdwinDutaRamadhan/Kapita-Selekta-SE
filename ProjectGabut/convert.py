import math
#Converter Suhu
def celciusToReamur(c):
    return 4/5*c
def celciusToFarenheit(c):
    return 9/5*c+32
def reamurToCelcius(r):
    return 5/4*r
def reamurToFarenheit(r):
    return 9/4*r+32
def farenheitToCelcius(f):
    return (f-32)*5/9
def farenheitToReamur(f):
    return (f-32)*4/9

#Converter Lusin, Kodi, Gross
def buahToLusin(buah):
    if buah % 12 == 0: return print(f"{buah} Buah = {int(buah/12)} Lusin")
    else: return print(f"{buah} Buah = {int(math.floor(buah/12))} Lusin {int(buah % 12)} Buah")
def buahToKodi(buah):
    if buah % 20 == 0: return print(f"{buah} Buah = {int(buah/20)} Kodi")
    else: return print(f"{buah} Buah = {int(math.floor(buah/20))} Kodi {int(buah % 20)} Buah")
def buahToGross(buah):
    if buah % 144 == 0: return print(f"{buah} Buah = {int(buah/144)} Gross")
    else: return print(f"{buah} Buah = {int(buah/144)} Gross {int(buah % 144)} Buah")
 

