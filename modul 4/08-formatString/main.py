# format string

"""
    string adalah kumpulan dari karakter 
    cara membuat string 
    1. dengan single quote '...'
    2. dengan double qupte "..."
"""

# membuat string dengan single quote
nama = 'nama saya lilla izati kamila'
print (nama)

# membuat string dengan double quote
nama = "nama saya lilla izati kamila"
print (nama)

print ("nama saya lilla")
print ("jangan lupa solat ya teman")

# maksa harus single quote
# pakai tanda \

print ('g\'day')
print ('what\,s up')
print ('c:\\user\\lila')

nama = "lila"
print ("selamat datang" , nama )

# format string 'f' dan '{}
format_str = f'selamat datang {nama}'
print (format_str) 

# format string angka 
angka = 2005.5  
format_str = f'angka={angka}'

# bilangan dengan ordo ribuan 
angka = 100 
format_str = f'jutaan = {angka:,}'
print (format_str)

# bilangan desimal
angka=200.2340
format_str = f'desimal= {angka:. 3f}'
print (format_str)

# persen 
angka = 0,55 #0,55 * 100 = 55
format_str = f'persen={angka:.22%}'
print(format_str)

# operasi arutmatika dengan format string
harga = 3547
jumlah = 3

print (f'total bayar: {harga*jumlah: ,}')