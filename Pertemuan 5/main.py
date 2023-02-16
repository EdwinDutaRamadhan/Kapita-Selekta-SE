# '''
# try:
# except Exception as e:

# else:
#     jika program masuk ke exception, maka tidak dijalankan else,
#     jika program tidak masuk ke exception, maka jalankan else
# finally:
#     jika program masuk ke exceptrion atau program tidak masuk ke exception,
#     maka jalankan finally
# '''

# angka = 0
# if angka == 0:
#     raise ValueError("Variable tidak boleh 0")
# else:
#     print("Nilai anda", str(angka))

class Kendaraan():
    def __init__(self,jenisKenadaraan):
        self.jenisKendaraan = jenisKenadaraan
    def __str__(self) -> str:
        return self.jenisKendaraan
    
class RodaDua(Kendaraan):
    def __init__(self,jenisKendaraan):
        super().__init__(jenisKendaraan)
class RodaEmpat(Kendaraan):
    def __init__(self,jenisKendaraan):
        super().__init__(jenisKendaraan)


kendaraanRodaDua = RodaDua("Honda")
print(kendaraanRodaDua.jenisKendaraan)
kendaraanRodaEmpat = RodaEmpat("Toyota")
print(kendaraanRodaEmpat.jenisKendaraan)
