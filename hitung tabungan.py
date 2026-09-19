import json
import os

print("======== Nabung Ayo ========")
print("==== kalo ada uang sisa ====")

FILE_DATA = "tabungan.json"
pemasukan = []
pengeluaran = []

if os.path.exists(FILE_DATA):
    try:
        with open(FILE_DATA, "r") as f:
            data = json.load(f)
            pemasukan = data.get("pemasukan", [])
            pengeluaran = data.get("pengeluaran", [])
        print(">> data lama ketemu, diload ya")
    except:
        pass

def simpan():
    with open(FILE_DATA, "w") as f:
        json.dump({"pemasukan": pemasukan, "pengeluaran": pengeluaran}, f)
    print("(kesimpen ke hp)")

def Pemasukan():
    jumlah = input("tambah tabungan:   ")
    jumlah = float(jumlah.replace(".", "").replace(",", ""))
    ket = input("uang bekas apa :  ")
    pemasukan.append({"jumlah": jumlah ,"keterangan": ket})
    simpan()
    print("uang masuk kecatet")
    
def Pengeluaran():
    jumlah = input("mau di pake berapa:   ")
    jumlah = float(jumlah.replace(".", "").replace(",", ""))
    ket = input("di pake buat apa :  ")
    pengeluaran.append({"jumlah": jumlah , "keterangan": ket})
    simpan()
    print("uang keluar kecatet")
    
def total_uang():
    masuk = sum(item["jumlah"] for item in pemasukan)
    keluar = sum(item["jumlah"] for item in pengeluaran)
    sisa = masuk - keluar
    
    print(f"Total pemasukan : Rp {masuk:,.0f}".replace(",", "."))
    print(f"Total pengeluaran : Rp {keluar:,.0f}".replace(",", "."))
    print(f"Sisa uang : Rp {sisa:,.0f}".replace(",", "."))
    
    if pemasukan:
        print("-- Rincian Masuk --")
        for i in pemasukan:
            print(f"+ Rp {i['jumlah']:,.0f} : {i['keterangan']}".replace(",", "."))
    if pengeluaran:
        print("-- Rincian Keluar --")
        for i in pengeluaran:
            print(f"- Rp {i['jumlah']:,.0f} : {i['keterangan']}".replace(",", "."))
    
    if sisa < 0:
       print("pengeluaran kebanyakan")
    elif sisa == 0:
       print("kga ada uang sisa")
    else:
        print("\nmantap bisa nabung")
    print("=========================")
    
def reset_data():
    konfirm = input("yakin mau hapus semua? (y/n): ").lower()
    if konfirm == "y":
        global pemasukan, pengeluaran
        pemasukan = []
        pengeluaran = []
        if os.path.exists(FILE_DATA):
            os.remove(FILE_DATA)
        print("udah ke-reset jadi 0 semua")
    else:
        print("gak jadi dihapus")
    
    
while True:
    print("\n1 : nambah tabungan")
    print("2 : ambil tabungan")
    print("3 : liat total tabungan")
    print("4 : reset/hapus tabungan")
    print("5 : keluar")
    
    pilih = input("pilih 1-5:  ")
    
    if pilih == "1":
       Pemasukan()
    elif pilih == "2":
       Pengeluaran()
    elif pilih == "3":
       total_uang()
    elif pilih == "4":
        reset_data()
    elif pilih == "5":
       print("Ok makasih udah nabung")
       break 
    else:
        print("salah pilih, coba lagi ya")