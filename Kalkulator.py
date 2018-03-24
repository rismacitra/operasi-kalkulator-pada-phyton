pembatas =  60

print  "#" * pembatas

nama = raw_input ("masukkan nama anda: ")
nim = raw_input ("masukkan nim anda: ")
print "\n"

print "selamat datang " ,nama, "dengan nim" ,nim , "diprogram kalkulator"
print "\n"

bil1 = int(raw_input ("masukkan bilangan ke1: "))
bil2 = int(raw_input ("masukkan bilangan ke2: "))
print "\n"
print "maka hasil program kalkulator"
print "\n"

def pertambahan():
    hasil = bil1+bil2
    print "hasil dari" ,bil1, "+" ,bil2, "=" ,hasil,
    print "\n"
    
def pengurangan():
    hasil = bil1-bil2
    print "hasil dari" ,bil1, "-" ,bil2, "=" ,hasil,
    print "\n"

def perkalian():
    hasil = bil1*bil2
    print "hasil dari" ,bil1, "*" ,bil2, "=" ,hasil,
    print "\n"
    
def pembagian():
    hasil = bil1/bil2
    print "hasil dari" ,bil1, "/" ,bil2, "=" ,hasil,
    print "\n"
    
pertambahan()
pengurangan()
perkalian()
pembagian()


