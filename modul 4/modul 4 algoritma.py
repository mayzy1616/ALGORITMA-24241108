# format string 

"""
    string : kumpulan dari karakter 
    cara membuat string : 
    1. dengan single qoute '...'
    2. dengan double quote "..."
"""
# membuat string dengan single qoute 
nama = 'nama saya mayzy nawang wulan'
print(nama)

# membuat string dengan double quote
nama = 'hasan wira yudha'
print(nama)

print("nama saya mayzy")
print("jangan lupa sholat")

# maksa harus single qoute
# pakai tanda \
print('g\'day')
print('what\'sUp!')

print('c:\\user\\mayzy')

nama = "mayzy"
print("selamat datang", nama)


# format string angka 
format_str = 'f selamat datang {nama}'
print(format_str)

# format string angka 
angka = 2005.5
format_str = f'angka = {angka}'
print(format_str)

#format string angka ribuan \
angka = 20000
format_str = f'jutaan = {angka}'
print(format_str)

# bilangan desimal 
angka = 2005.54321
format_str = f'desimal = {angka}'
print(format_str)

# persen %
angka = 0.55 # 0.55 * 100 = 55%
format_str = f'persen = {angka}'
print(format_str)

# operasi aritmatika dengang format string 
harga = 57250  
jumlah = 3

print(f'total bayar : {harga*jumlah:,}')
