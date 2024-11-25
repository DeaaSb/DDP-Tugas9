print ('## Nomor 1 ##')
def celcius_ke_fahrenheit(celcius):
    fahrenheit=(celcius*9/5)+32
    return fahrenheit

suhu_celcius1 = 0
suhu_celcius2 = 100
suhu_fahrenheit1 = celcius_ke_fahrenheit (suhu_celcius1)
print('Suhu Celcius', suhu_celcius1, 'sama dengan', suhu_fahrenheit1)

suhu_fahrenheit2 = celcius_ke_fahrenheit (suhu_celcius2)
print('suhu_celcius', suhu_celcius2, 'sama dengan', suhu_fahrenheit2)

print()
print ('## Nomor 2 ##')
def genap_ganjil(bilangan):
    hitung = bilangan % 2 == 0 
    return hitung

angka = 4
hasil = genap_ganjil(angka)
print(f"Bilangan {angka} bernilai {hasil}")

angka2 = 7 
hasil2 = genap_ganjil(angka2)
print(f"Bilangan {angka2} bernilai {hasil2}")

print()
print('## Nomor 3 ##')

def cek_kelulusan(nilai):
    if nilai >= 60:
        return 'Lulus'
    else:
        return 'Gagal'
    
nilai_kamu = 50
status = cek_kelulusan(nilai_kamu)
print(f"Nilai: {nilai_kamu}, Status: {status}")

nilai_kamu2 = 90
status2 = cek_kelulusan(nilai_kamu2)
print(f"Nilai: {nilai_kamu2}, Status: {status2}")
    
    
print()
print('## Nomor 4 ##')
def bilangan(angka):  
    ganjil = [str(i) for i in range(1, angka) if i % 2 != 0]  
    print(",".join(ganjil))  
bilangan(20)  