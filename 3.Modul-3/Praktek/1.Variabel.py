import datetime as dt

tanggal = int(input("Tanggal \t: "))
print(type(tanggal))
bulan = int(input("Bulan \t\t: "))
print(type(bulan))
tahun = int(input("Tahun \t\t: "))
print(type(tahun))


tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(tanggal_lahir)
print(type(tanggal_lahir))

hari_ini = dt.date.today()
print(hari_ini)

umur_hari = hari_ini - tanggal_lahir
print(umur_hari.days)
umur_tahun = umur_hari.days // 365
print(umur_tahun)
umur_bulan = umur_hari.days % 365 
print(umur_bulan)
umur_bulan_sisa = umur_bulan // 30
print(umur_bulan_sisa)

print(f"\nUmur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")