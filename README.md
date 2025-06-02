# TASK-REPOSITORY
_______________________________________________
![alt text](https://github.com/Denny-Risnandar/TASK-REPOSITORY/blob/main/1_tIzqPBxnAID8i5_7ZVK5TQ.png)

______________________________________________________
_di buat untuk laporan sesi 3 tanggal 1 juni 2025 (Pembahasan tentang :
Chapter 5: Pengkondisian (If-Else), dan 2 
Chapter 6: Perulangan (For dan While),  
seru sangat menarik sob. . fungsi ini di implementasikan dengan rumus sehari hari yang bisa bikin " oh ternyata gini . . " yuk lanjut

kali ini akan di implementasi kan untuk nyari "Tahun Kabisat"  apakah tahun tersebut merupakan tahun Kabisat atau bukan ?
dan untuk mencari di tanggal tersebut adalah "Hari apa". .  yang selama ini kita bisa menggunakan kalender di HP atau di PC nah skrang kita buat aplikasi sederhana nya. oh iya udh tau belum sob siapa penemu dari rumus ini ??? yappzzz namanya Christian Zeller pada abad ke-19 untuk menghitung hari dalam minggu tersebut (dalam kaleder Gregorian / Masehi atau kalender Julian ), karena penemunya Christian Zeller, maka rumus nya di sebut nya "Zeller's congruence".
rumus nya sih gini :
![alt text](https://github.com/Denny-Risnandar/TASK-REPOSITORY/blob/main/zellers-200628000123-thumbnail.webp?raw=true)

Terlihat Pusing yaa sob, tenang kita rubah aja kebentuk bahasa pyton yaa. .

_________________________________________
Gabungan rumus Pengkondisian (If-Else) dan Perulangan (For dan While)

yg pertama kita buat untuk tampilan perintah inputan tanggal, 

 ini untuk validasi tanggal
 
 tanggal = int(input('masukan tanggal (1-31): '))

  if tanggal <1 or tanggal >31 :
  
 print('tanggal harus antara 1 dan 31, sekali lagi input yaa') 
 
 continue

penjelasan : 

tanggal = kita buat sebagai variabel yang  isinya adalah = int(input('masukan tanggal (1-31:  ') angka tersebut menjadi integer / angka,

pake rumus if, jika tanggal kurang dari 1 atau tanggal lebih dari angka 31 , maka sistem akan menampilkan "tanggal harus di isi antara angka 1 dan 31"

continue = sistem akan menampilkan untuk penginputan variabel yang kedua, yaitu untuk variabel bulan.

lakukan hal yang sama untuk  membuat variabel bulan :

bulan = int(input('masukan bulan (1-12): '))

if bulan <1 or bulan >12 :

print('bulan harus antara 1 dan 12')

continue

(Penjelasan sama ya sob, namun ini untuk bulan)

selanjut nya buat kembali untuk mebuat variabel Tahun :

tahun =int(input('masukan tahun : '))

if tahun <1:

print('tahun harus angka positif')

continue

return tanggal, bulan, tahun

except ValueError:

print('harus masukan angka bro')

tanggal, bulan, tahun = Validasi_input ()

print(f'input valid: {tanggal}//{bulan}//{tahun}')

Nah pada setelah pembuatan variabel tahun, sistem akan menambahkan perintah "continue" dan "except ValueError" artinya jika ada kesalahan dalam penginputan pada variabel tanggal, bulan , atau tahun sistem akan membaca kembali ke awal pengisian variabel yaitu ke variabel tanggal kembali dengan menampilkan perintah "harus masukan angka bro"

selanjutnya variabel yang kita buat tadi dan yang nantinya akan kita input bisa kita gunakan kembali dengan cara memanggil 3 variabel tersebut sekligus tanpa harus mengetik ulang kembali, nah pyton menyediakan fungsi tersebut namanya fungsi "def", sehingga variabel tanggal, bulan, tahun = validasi_input

jika penginputan pada variable tanggal, bulan , tahun sesuai maka sistem akan menampilkan tampilan " input valid = tanggal, bulan, tahun yang telah kita input.







