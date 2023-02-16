# 1. Buatlah fungsi untuk menghitung total bilangan pada list, tidak boleh pakai built in function
#    input  : list bilangan
#    output : total bilangan (int)
def hitungTotalList(listInput):
    total = 0
    panjangList = len(listInput)+1
    for x in range(panjangList):
        total += x
    return print(int(total))
# 2. Buatlah fungsi untuk menghitung volume balok
#    input : panjang, lebar , tinggi (int)
#    output: volume balok (int)

def hitungVolumeBalok(panjang, lebar, tinggi):
    return print(int(panjang*lebar*tinggi))


# 3. Buatlah fungsi untuk mencetak kalimat perkenalan seperti berikut:
#    "Halo, nama saya {} dan saya berasal dari {kota asal}" 
#    input  : nama
#    output : print string 
def kalimatPerkenalan(nama="Edwin", kota="Salatiga"):
    return print(f"Halo, nama saya {nama} dan saya berasal dari {kota}")


# 4. Buatlah fungsi untuk membuat kalimat panjang dari sebuah list
#    input  : list string
#    output : string

def concatListValue(listInput):
    displayListInput = " ".join(str(x) for x in listInput)
    return print(displayListInput)


# 5. Buatlah fungsi untuk mencetak bilangan ganjil yang ada pada sebuah list
#    input  : list bilangan
#    output : print list bilangan ganjil

def sumBilanganGanjil(listInput):
    panjangList = len(listInput)+1
    for i in range(panjangList):
        if i % 2 == 1:
            print(i)


def total(*bilangan, **keywords):
    hitung = 0

    #ini proses ekseskusi dari variable args "Bialngan"
    for bil in bilangan:
        hitung += bil

    #ini proses eksekusi dari variabel kwargs (keyword argument)
    for key in keywords:
        hitung += keywords[key]
        
    
    return hitung

print(total(1,2,3,4,5,)) #versi boleh berapa aja parameter yang masuk
print(total(daging=2, sayur=10, buah=3)) # versi parameter apa aja yang boleh masuk
print("Versi gabungan : " , total(7,8,5, sayur=10,buah=3,daging=2))#versi gabungan + kwargs dibalik

def contohKwargs(**kwargs):
    varParamA = kwargs.get('paramA', 100)
    print(varParamA)

contohKwargs(paramA=200)#hasil 200
contohKwargs()