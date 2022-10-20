Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

girdi = input("Soruyu Çözmek İçin Rastgele Bir Kat Sayısı Giriniz..")
basamak = input("Basamak giriniz.")
print("Rakamları toplamının",girdi," katına eşit olan iki basamaklı kaç tane doğal sayı vardır?");
syc = 0
sayiAr = []
for sayi in range (10**(int(basamak)-1),10**int(basamak)):
    bastop = 0
    for x in str(sayi):
        bastop += int(x)
    if (sayi == (bastop)*int(girdi)):
        sayiAr.append(sayi)
        syc += 1
        
print(syc," tane doğal sayı vardır.",sayiAr)
		  