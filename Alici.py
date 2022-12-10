# Yine kütüphanemizi dahil ettik. Daha sonra göndericiden gelen mesajı açtık.
#Açık anahtar, mesaj, imzalı mesajı ayrı olarak doğrulamak için değişkenlerde saklıyoruz.

import rsa

def dosyayioku(dosya):
    dosya_a = open(dosya, 'rb')
    icerik = dosya_a.read()
    dosya_a.close()
    return icerik

acikanahtar = rsa.PublicKey.load_pkcs1(dosyayioku('acikanahtar.key'))

mesaj = dosyayioku('mesaj')
imzalimesaj = dosyayioku('imzalimesaj')


# Doğrulama için mesaj, imzalimesaj ve acikanahtar kullanılarak RSA kütüphanesinin doğrulama fonksiyonunu kullanıyoruz.

try:
    rsa.verify(mesaj, imzalimesaj, acikanahtar)
    print("Doğrulama Başarıyla Tamamlandı.")

except:
    print("Doğrulama Gerçekleştirilemedi!")
