import rumah

x = rumah(5, 5, 6)


print("Lebar: ", x.lebar)
x.lebar=5
print("Lebar: ", x.lebar)
luas = x.hitung_luas()
volume = x.hitung_volume()
print("Luas permukaan rumah: ", luas)
print("Volume rumah: ", volume)