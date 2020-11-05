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