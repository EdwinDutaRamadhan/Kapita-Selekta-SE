import volume as vol
# 1. Buatlah sebuah fungsi untuk mencari bilangan prima yang ada pada range bilangan tertentu
#    input  : nilai awal, nilai akhir
#    output : list bilangan prima

def isPrime(val):#apakah val merupakan prima
   for i in range(2, val):#2 prima pertama, 2..val-1
      if val % i == 0:
         return False
   return True

def getPrimeInRange(start, end):#end must be greater than start
   primeList = []
   for i in range(start, end+1):
         if isPrime(i):
            primeList.append(i)
   return primeList

print("Soal 1 Prima :", getPrimeInRange(5,20))

# 2. Buatlah fungsi untuk mencari bilangan ganjil pada range bilangan tertentu
#    input  : nilai awal, nilai akhir
#    output : list bilangan ganjil
def getOddInRange(start, end):
   oddList = []
   for i in range(start, end+1):
      if i % 2 == 1:
         oddList.append(i)
   return oddList
print("Soal 2 Ganjil : ",getOddInRange(5,20))

# 3. Buatlah fungsi untuk mencari bilangan prima ganjil pada range bilangan tertentu, gunakan fungsi dari
#    soal pertama dan kedua untuk membuat fungsi ini
#    input  : nilai awal, nilai akhir
#    output : list bilangan prima ganjil

def getOddPrimeInRange(start, end):
   oddPrime = []
   for i in range(start, end+1):
      if isPrime(i) and i % 2 == 1:
         oddPrime.append(i)
   return oddPrime

print("Soal 3 GanjilPrima : ", getOddPrimeInRange(5,20))

# 4. Buatlah fungsi untuk membalikkan karakter pada string
#    input  : string
#    output : string yang telah dibalik
#    Contoh : input -> "salatiga", output -> "agitalas"

def reverseString(inputString):
   return inputString[::-1]

print("Soal 4 ReverseString : ", reverseString("Kasur"))

# 5. Buatlah fungsi untuk mengecek apakah suatu string adalah palindrome/tidak, boleh menggunakan fungsi dari soal
#    nomor 4 untuk mempermudah dalam membuat fungsi
#    input  : string
#    output : boolean
#    Contoh : "kasur rusak"

def isPalindromeString(inputString):
   return inputString == inputString[::-1]

print("Soal 5 isPalindrome : ", isPalindromeString("kasur rusak"))

# 6. Buatlah fungsi untuk mencari selisih nilai tertinggi dan terendah bilangan pada sebuah list
#    input  : list bilangan
#    output : selisih bilangan tertinggi & terendah

def getListMinMaxDifference(inputList):
   return max(inputList) - min(inputList)

print("Soal 6 listMinMaxDifference : ", getListMinMaxDifference([5,1,2,7,9,12]))

# 7. Buatlah fungsi untuk menghitung jumlah huruf vokal dan konsonan yang ada pada sebuah string
#    input  : string
#    output : list/tuple jumlah huruf vokal dan konsonan

def getSumVocalConsonantFromString(inputString):
   totalVocal = 0
   totalConsonant = 0
   inputString = inputString.lower() #force inputString to lower case
   for i in inputString:
      if i in ["a","i","u","e","o"] : totalVocal +=1
   totalConsonant = len(inputString) - totalVocal
   return totalVocal,totalConsonant

print("Soal 7 VocalConsonant: ",getSumVocalConsonantFromString("Edwin"))

# 8. Buatlah fungsi untuk mencari bilangan tertentu beserta indexnya pada sebuah list
#    input  : list bilangan, bilangan yang dicari
#    output : dictionary {'status': boolean status hasil pencarian, 'index': index element}

def searchNumberFromList(inputList, keyword):
   for i in inputList:
      if i == keyword : return {"status" : True, "index" : i-1} 
   return {"status" : False, "index" : "not found"}

print("Soal 8 SearchFromList :",searchNumberFromList([1,2,3,4,5], 2))

# 9. Buatlah fungsi aritmatika dengan 3 parameter (operator, bilangan 1, bilangan 2) dengan default value bilangan
#    bernilai 1 yang dapat melakukan operasi penjumlahan, pengurangan, perkalian, dan pembagian
#    Pada fungsi tersebut gunakan exception untuk memberi tahu user jika salah ketika memberikan input operator,
#    terdapat zero division error, dsb
#    input  : operator (str), bilangan 1, (int) bilangan 2 (int)
#    output : hasil operasi aritmatika

def aritmatika(operator, bilangan1=1, bilangan2=1):
   if(validasiOperator(operator)):
      try:
         if "+" in operator: return bilangan1 + bilangan2 #Pertambah
         elif "-" in operator: return bilangan1 - bilangan2 #Pengurangan
         elif "*" in operator: return bilangan1 * bilangan2 #Perkalian
         elif "/" in operator: return bilangan1 / bilangan2 #Pembagian
      except Exception as e: 
         return "Error "+str(e)
   else: 
      return "Operator harus +,-,*,/ !"
def validasiOperator(operator): #fungsi filter operator inputan user
   for i in operator:
      if i == "+" or i == "-" or i == "*" or i == "/": #Return true if operator = +,-,*,/
         return True 
   return False

print("Soal 9 Aritmatika : ",aritmatika("1",0,0))
# # volume.py
# 10. Buatlah modul bernama volume.py, buat fungsi untuk menghitung volume
#    kubus, balok, limas segi 4, dan prisma segi 3. Kemudian panggil fungsi" tersebut
#    pada main.py

print("Soal 10  \nKubus : ", vol.getVolumeKubus(sisi=10))
print("Balok : ", vol.getVolumeBalok(panjang=8,lebar=12,tinggi=10))
print("Limas Segi Empat : ", vol.getVolumeLimasSegiEmpat(sisi=10,tinggi=15))
print("Prisma Segi Tiga : ", vol.getVolumePrismaSegiTiga(panjang=4,lebar=3,tinggi=7))
# Kumpulkan paling lambat tgl 14 Februari 2023 pukul 17.00 dalam bentuk zip
# Nama file Tugas2_NIM.zip