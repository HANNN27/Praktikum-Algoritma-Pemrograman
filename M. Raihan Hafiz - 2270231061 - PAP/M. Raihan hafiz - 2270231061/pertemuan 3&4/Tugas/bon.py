import os
import time
os.system('cls')
barang = []
harga = []
total_barang = []
total = 0

print('=' * 17 + 'SELAMAT DATANG' + '=' * 17)

nama = input('\tNama \t\t: ')
alamat = input('\tAlamat \t\t: ')
noTelp = int(input('\tNo Telp \t: '))

while True :
    print('=' * 15 + 'SELAMAT BERBELANJA' + '=' * 15)
    print('=' * 17 + 'DAFTAR BARANG' + '=' * 18)
    print("""         No | Nama Barang | Harga
        ----------------------------
        1   | CPU         | Rp.4,7 Jt
        2   | MONITOR     | Rp.2 Jt
        3   | MOUSE       | Rp.270000
        4   | HEADSET     | Rp.300000
        5   | MOUSE PAD   | Rp.70000
        6   | MOTHERBOARD | Rp.1 Jt
        7   | M/KEYBOARD  | Rp.950000
        8   | RAM         | Rp.1,7 Jt""")
    print('\t----------------------------')
    print()
    print(f'\t     ~ Hello {nama} ~ >_<')
    print()
    kode = int(input('\tMasukan Kode Barang   : '))
    jumlah_barang = int(input('\tMasukan Jumlah Barang : '))
    if kode == 1 :
        barang.append('CPU')
        jumlah = 4700000 * jumlah_barang
        total_barang.append(jumlah_barang)
        total += jumlah
        harga.append(jumlah)
    elif kode == 2 :
        barang.append('MONITOR')
        jumlah = 2000000 * jumlah_barang
        total_barang.append(jumlah_barang)
        total += jumlah
        harga.append(jumlah)
    elif kode == 3 :
        barang.append('MOUSE')
        jumlah = 270000 * jumlah_barang
        total_barang.append(jumlah_barang)
        total += jumlah
        harga.append(jumlah)
    elif kode == 4 :
        barang.append('HEADSET')
        jumlah = 300000 * jumlah_barang
        total_barang.append(jumlah_barang)
        total += jumlah
        harga.append(jumlah)
    elif kode == 5 :
        barang.append('MOUSE PAD')
        jumlah = 70000 * jumlah_barang
        total_barang.append(jumlah_barang)
        total += jumlah
        harga.append(jumlah)
    elif kode == 6 :
        barang.append('MOTHERBOARD')
        jumlah = 1000000 * jumlah_barang
        total_barang.append(jumlah_barang)
        total += jumlah
        harga.append(jumlah)
    elif kode == 7 :
        barang.append('M/KEYBOAR')
        jumlah = 950000 * jumlah_barang
        total_barang.append(jumlah_barang)
        total += jumlah
        harga.append(jumlah)
    elif kode == 8 :
        barang.append('RAM')
        jumlah = 1700000 * jumlah_barang
        total_barang.append(jumlah_barang)
        total += jumlah
        harga.append(jumlah)
    lanjut = str(input('\tLanjut Belanja y/n ?  : '))
    if lanjut == 'n':
        break

a = total
if a > 4000000 :
    diskon = a * (10 / 100)
else :
    diskon = a * (5 / 100)

setelah_diskon = total - diskon

tanggal = time.strftime("%d-%m-%y %H:%M:%S")

print('='*10 + 'TERIMA KASIH TELAH BELANJA DI TOKO KAMI' + '='*10)
print(f'\tNama \t\t: {nama}')
print(f'\tNo Telp \t: {noTelp}')
print(f'\tAlamat \t\t: {alamat}')
print(f'\tTanggal \t: {tanggal}')
print(f'\tDaftar \t\t: {barang}')
print(f'\tJumlah \t\t: {total_barang}')
print(f'\tHarga \t\t: {harga}')
print(f'\tTotal \t\t: {total}')
print('\tDiskon \t\t: {}' .format(int(diskon)))
print('\tSetelah Diskon  : {}' .format(int(setelah_diskon)))

uang = int(input('\tJumlah Uang \t: '))
if uang > setelah_diskon :
    print(f'\tKembalian \t: {uang - setelah_diskon}')
elif uang == setelah_diskon :
    print(f'\tUANG ANDA PAS')
elif uang < setelah_diskon :
    print(f'\tUang Kurang \t: {setelah_diskon - uang}')
print('='*15 + 'JANGAN LUPA MAMPIR KEMBALI' + '='*15)