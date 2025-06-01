# calculator tanggal, cek kabisat dan hitung hari dng loop
def Validasi_input ():
    while True:
        try:
            #ini untuk validasi tanggal
            tanggal = int(input('masukan tanggal (1-31): '))
            if tanggal <1 or tanggal >31 :
                print('tanggal harus antara 1 dan 31, sekali lagi input yaa') 
                continue
            #ini untuk validasi bulan
            bulan = int(input('masukan bulan (1-12): '))
            if bulan <1 or bulan >12 :
                print('bulan harus antara 1 dan 12')
                continue
            #ini untuk validasi tahun
            tahun =int(input('masukan tahun : '))
            if tahun <1:
                print('tahun harus angka positif')
                continue
            return tanggal, bulan, tahun
        except ValueError:
            print('harus masukan angka bro')
tanggal, bulan, tahun = Validasi_input ()
print(f'input valid: {tanggal}//{bulan}//{tahun}')

# SELANJUTNYA MINTA INPUT VALIDITAS
print('masukan tanggal untuk cek hari tersebut dan apakah masuk ke tahun kabisat: ')
tanggal, bulan, tahun = Validasi_input()

# SELANJUTNYA UNTJUK MENGECEK KABISAT UNTUK RENTANG TAHUN
print("\nCek tahun kabisat untuk rentang tahun:")
for i in range(tahun - 2, tahun + 3):
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print(f"Tahun {i} adalah tahun kabisat!")
    else:
        print(f"Tahun {i} bukan tahun kabisat!")

# PAKE RUMUS ZELLER CONGRUENCE
if bulan == 1 or bulan == 2:
    bulan += 12
    tahun -= 1
K = tahun % 100
J = tahun // 100
h = (tanggal + ((13 * (bulan + 1)) // 5) + K + (K // 4) + (J // 4) - 2 * J) % 7
print('\nhasil perhitungan hari: ')
if h == 0:
    print(f'tanggal {tanggal}//{bulan}, {tahun} adalah hari sabtu')
elif h == 1:
    print(f'tanggal {tanggal}//{bulan}, {tahun} adalah hari minggu')
elif h == 2:
    print(f'tanggal {tanggal}//{bulan},  {tahun} adalah hari senin')
elif h == 3:
    print(f'tanggal {tanggal}//{bulan}, {tahun} adalah hari selasa')
elif h == 4:
    print(f'tanggal {tanggal}// {bulan}, {tahun} adalah hari rabu')
elif h == 5:
    print(f'tanggal {tanggal}// {bulan},  {tahun} adalah hari kamis')
else:
    print(f'tanggal {tanggal}//{bulan}//  {tahun} adalah hari jumat')

