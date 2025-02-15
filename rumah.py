# class rumah:
#     def __init__(self, panjang, lebar, tinggi, color):
#         self.panjang = panjang
#         self.lebar = lebar
#         self.tinggi = tinggi
#         self.color = color



#     def hitung_luas(self):
#         return 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)

#     def hitung_volume(self):
#         return self.panjang * self.lebar * self.tinggi
    
# panjang = float(input("Masukkan panjang: "))
# lebar = float(input("Masukkan lebar: "))
# tinggi = float(input("Masukkan tinggi: "))

# rumah = Rumah(5, 5, 6)


# print("Lebar: ", rumah.lebar)
# rumah.lebar=5
# print("Lebar: ", rumah.lebar)
# luas = rumah.hitung_luas()
# volume = rumah.hitung_volume()
# print("Luas permukaan rumah: ", luas)
# print("Volume rumah: ", volume)

class Rumah:
    
    def __init__(self, alamat, jumlah_kamar, warna, luas, sah, harga):
        self.alamat = alamat
        self.jumlah_kamar = jumlah_kamar
        self.warna= warna
        self.sah= sah
        self.luas = luas
        self.harga = harga


    def tampilkan_info(self):
        status="Sah"
        if self.sah :
            status= "sah" 
        else:
            status="TIdak Sah"
        
        info = f"Rumah ini berlokasi di: {self.alamat}, memiliki {self.jumlah_kamar} kamar, warna {self.warna}, luas {self.luas} m², dan harganya Rp {self.harga:,}. Status: {status}"
            # "alamat: {self.alamat}",
            # "jumlah Kamar: {self.jumlah_kamar}",
            # "warna: {self.warna}",
            # "luas: {self.luas} m²",
            # "harga: Rp {self.harga:,}"
        
        return info
    

rumahku = Rumah("Jalan Tun Ismail", 7, "Putih", 120 , False, 750000000)

print(rumahku.tampilkan_info())