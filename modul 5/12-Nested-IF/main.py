# Percabangan Bersarang - nasted IF

# Kalkulator sederhana
print(20*"=")
print("kalkulator sederhana")
print(20*"=")

angka_1 = float(input("masukan angka ke-1 ="))
operator = input ("operator (+,-)=")
angka_2 = float(input("masukan angka ke-2 ="))

#percabangan
if operator == '+' :
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah ={hasil}")
elif operator == '_':
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah ={hasil}")
else :
    print("tolong masukan angka yang benar dan operator yang benar")
