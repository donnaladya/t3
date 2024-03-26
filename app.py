# hitung luas segitiga seerhana
def luas_segitiga():
    a = int(input("masukkan alas segitiga: "))
    t = int(input("masukkan tinggi segitiga: "))
    luas = a * t /2
    print("luas segitiga adalah:",luas)

luas_segitiga()

#hitung luas persegi panjang
def luas_persegi_panjang():
    p = int(input("masukkan panjang persegi: "))
    l = int(input("masukkan lebar persegi: "))
    luas = p * l
    print("luas persegi adalah: ", luas)
    
luas_persegi_panjang()

# hitung luas lingkaran
def luas_lingkaran():
    r = int(input("masukkan jari-jari lingkaran: "))
    luas = 3.14 * r * r
    print("luas lingkaran adalah: ",luas)

luas_lingkaran()
