# percabangan 
# menggunakan statmen if

# struktur
"""
   1. if-nya
   2. ada kondisi (bernilai true/false)
   3. ada aksi -> proses lanjutan
"""

nama = input ("masukan nama anda =")

# if statmen dalam bentuk inline (satu baris)
if nama == "romy" : print (f"selamat datang{nama}")
print ("terima kasih")

# if stateman dalam bentuk identasi
if nama == 'romy':
    print (f'selamat datang {nama}')
    print ("terimakasih")

# IF - ELSE statemant
if nama == 'romy' : 
    # aksi 1
    print (f'selamat datang {nama}')
else :
    #aksi 2
    print (f' kamu {nama},bukan romy')
print ('terima kasih')
