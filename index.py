#main menu
def menu():
    #menu-judul
    print("=======================================================")
    print("   Program Menghitung Luas dan Keliling Bangun Datar   ")
    print("=======================================================")

    #menu-pilihan
    print("Daftar Bangun Datar : \n")
    print(" 1. Luas Bujur Sangkar \n 2. Keliling Bujur Sangkar \n 3. Luas Persegi Panjang \n 4. Keliling Persegi Panjang \n 5. Luas Segitiga \n 6. Keliling Segitiga \n 7. Luas Lingkaran \n 8. Keliling Lingkaran \n 9. Keluar \n")

#fungsi bangun datar
def luas_buj_sang(s):    
    l = s*s
    return l
    
def kel_buj_sang(s):
    k = 4*s
    return k

def luas_persegi_pjg(p,l):
    L = p*l
    return L
    
def kel_persegi_pjg(p,l):
    k = 2*(p+l)
    return k
    
def luas_segitiga(a,t):
    l = (a*t)/2
    return l

def kel_segitiga(a,b,c):
    k = a+b+c
    return k

def luas_ling(r):
    l = 3.14*r*r
    return l
    
def kel_ling(r):
    k = 2*3.14*r
    return k

ulang = 'y'
while(ulang == 'y'):

    menu()

    pil = int(input("Masukkan pilihan Anda = "))

    #Luas Bujur Sangkar
    if pil == 1:
        print("-------------------------------")
        print("Anda memilih Luas Bujur Sangkar")
        print("-------------------------------")
        s = float(input("Masukkan sisi (cm) = "))
        print("Luas Bujur Sangkar = %f" %luas_buj_sang(s), "cm2") 

    #Keliling Bujur Sangkar
    elif pil == 2:
        print("-----------------------------------")
        print("Anda memilih Keliling Bujur Sangkar")
        print("-----------------------------------")
        s = float(input("Masukkan sisi (cm) =  "))
        print("Keliling Bujur Sangkar = %f" %kel_buj_sang(s), "cm2")

    #Luas Persegi Panjang
    elif pil == 3:
        print("---------------------------------")
        print("Anda memilih Luas Persegi Panjang")
        print("---------------------------------")
        p = float(input("Masukkan panjang (cm) =  "))
        l = float(input("Masukkan lebar (cm) =  "))
        print("Luas Persegi Panjang = %f" %luas_persegi_pjg(p,l), "cm2")

    #Keliling Persegi Panjang
    elif pil == 4:
        print("-------------------------------------")
        print("Anda memilih Keliling Persegi Panjang")
        print("-------------------------------------")
        p = float(input("Masukkan panjang (cm) =  "))
        l = float(input("Masukkan lebar (cm) =  "))
        print("Keliling Persegi Panjang = %f" %kel_persegi_pjg(p,l), "cm2")

    #Luas Segitiga
    elif pil == 5:
        print("--------------------------")
        print("Anda memilih Luas Segitiga")
        print("--------------------------")
        a = float(input("Masukkan alas (cm) =  "))
        t = float(input("Masukkan tinggi (cm) =  "))
        print("Keliling Persegi Panjang = %f" %luas_segitiga(a,t), "cm2")

    #Keliling Segitiga
    elif pil == 6:
        print("------------------------------")
        print("Anda memilih Keliling Segitiga")
        print("------------------------------")
        a = float(input("Masukkan sisi a (cm) =  "))
        b = float(input("Masukkan sisi b (cm) =  "))
        c = float(input("Masukkan sisi c (cm) =  "))
        print("Luas Segitiga = %f" %kel_segitiga(a,b,c), "cm2")

    #Luas Lingkaran
    elif pil == 7:
        print("---------------------------")
        print("Anda memilih Luas Lingkaran")
        print("---------------------------")
        r = float(input("Masukkan jari-jari (cm) =  "))
        print("Luas Lingkaran = %.f" %luas_ling(r), "cm2")

    #Keliling Lingkaran
    elif pil == 8:
        print("-------------------------------")
        print("Anda memilih Keliling Lingkaran")
        print("-------------------------------")
        r = float(input("Masukkan jari-jari (cm) =  "))
        print("Keliling Lingkaran = %.f" %kel_ling(r), "cm2")

    #keluar
    elif pil == 9:
        ulang = "t"

    ulang = input("Apakah Anda ingin menghitung ulang? [y/t]")
    if(ulang == 't'):
        print("\n Keluar")
