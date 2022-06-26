print("""

Hesap Makinesi

Toplamak için +
Çıkartmak için -
Çarpmak için *
Bölmek için / tuşlayınız

""")
sayi1 = int(input("sayi1 giriniz: "))
sayi2 = int(input("sayi2 giriniz: "))
islem = str(input("Yapmak istediğiniz işlemi seçiniz: "))

if islem == "+":

    print("Sonuç:", sayi1 + sayi2)
elif islem == "-":

    print("Sonuç:", sayi1 - sayi2)
elif islem == "*":

    print("Sonuç:", sayi1 * sayi2)
elif islem == "/":

    print("Sonuç:", sayi1 / sayi2)
else:
    print("geçersiz işlem girdiniz...")