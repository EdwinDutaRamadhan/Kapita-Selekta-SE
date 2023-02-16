priceTuple = (10000, 13000, 8000, 9000, 16000)
fruitTuple = ('mangga', 'apel', 'jeruk', 'semangka', 'anggur')

# Soal 1
# Buatlah dictionary dengan nama fruitDict dari kedua tuple di atas sehingga menjadi
# {'mangga': 10000, 'apel': 13000, dst...}
fruitDict = dict(zip(fruitTuple,priceTuple)) #zipped 2 tuple to dictionary
print("\nSoal 1 FruitDict : ")
print(fruitDict)

# Soal 2
# Dari dictionary fruitDict yang sudah terbuat, hitunglah rata-rata harga buah
print("\nSoal 2 FruitDictAverageValue : " + str(sum(fruitDict.values()) / int(len(fruitDict)))) # Average fruitDictValues cast to String
# ==================================================================================

# Soal 3
test_list = [4, 1, {'tiga': 3, 'tujuh': 7}, (9, 8, [2, 5]), 6]
# Dari test_list di atas, buatlah sebuah string dengan isi : '1 2 3 4 5 6 7 8 9'
print("\nSoal 3 List : ")
test_list_sorted = test_list[1] ,test_list[3][2][0] ,test_list[2]["tiga"] , test_list[0] ,test_list[3][2][1]  ,test_list[4] ,test_list[2]["tujuh"] ,test_list[3][1] ,test_list[3][0]
testListCastToString = " ".join(str(x) for x in test_list_sorted) #cast list to string with joining space each other
print(testListCastToString)

# Soal 4
# Dari string tersebut pecahlah kembali menjadi sebuah list yang berisi integer, kemudian hitung nilai total dari isi list
print("\nSoal 4 SortedListTotal : ")
print(sum(list(map(int, testListCastToString.split())))) # sum list where testListCastToString was convert from StringList to IntegerList
# ==================================================================================

str1 = "teknik informatika fakultas teknologi informasi universitas kristen satya wacana"
str2 = "sedang belajar bahasa pemrograman"
tupleMahasiswa = ('DEVA', 'IVAN')
dictKelas = {'IF001': 'Kapita Selekta', 'IF002': 'Matematika Diskrit', 'IF003': 'Pemrograman Web'}
listPython = ['p', 'y', 't', 'h', 'o', 'n']
# Soal 5
# Dari variable di atas, buatlah string sebagai berikut
# - 'Hari ini Deva tidak mengikuti mata kuliah Pemrograman Web'
# - 'Matematika Diskrit IF002 adalah salah satu mata kuliah di progdi Teknik Informatika Universitas Kristen Satya Wacana'
# - 'Ivan belajar bahasa pemrograman Python di mata kuliah Kapita Selekta'
print("\nSoal 5 SlicingVariable : ")
slicingString1 = "Hari ini " + tupleMahasiswa[0] + " tidak mengikuti mata kuliah " + dictKelas["IF003"]
slicingString2 = dictKelas["IF002"] + " " + list(dictKelas)[1] + " salah satu mata kuliah di progdi " + str1[:18].title() + str1[47:].title()
slicingString3 = tupleMahasiswa[1] + str2[6:] + " " + "".join(str(x) for x in listPython).title() + " di mata kuliah " + dictKelas["IF001"]
print(" - " + slicingString1 + "\n - " + slicingString2 + "\n - " + slicingString3)

listHari = ['Senin', 'Rabu', 'Jumat', 'Sabtu']
# Soal 6
# Tambahkan hari 'Selasa', 'Kamis', dan 'Minggu', sehingga listHari tersebut menjadi ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
print("\nSoal 6 Lists : ")
listHari.insert(1, "Selasa")
listHari.insert(3, "Kamis")
listHari.append("Minggu")
print(listHari)

# Soal 7
# Hapus hari 'Sabtu' dan 'Minggu' dari listHari, kemudian copy list listHari ke variable tupleHariKerja dengan tipe data tuple
print("\nSoal 7 Lists to Tuple : ")
listHari.remove("Sabtu")
listHari.pop(5)

def convertListToTuple(list): #definitions function return value tuple where parameter list
    return tuple(list)

print(convertListToTuple(listHari))