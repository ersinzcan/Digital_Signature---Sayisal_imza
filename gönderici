# Şifrelemede RSA kullanacağımız için RSA kütüphanesini ekledik.
# Dosyaları okumak için bir fonksiyon oluşturduk ve imzalama yapmak için anahtarlar oluşturduk.

import rsa

def dosyayioku(dosya):
    dosya_a = open(dosya, 'rb')
    icerik = dosya_a.read()
    dosya_a.close()
    return icerik
(acikanahtar, gizlianahtar) = rsa.newkeys(2048)


# Oluşturduğumuz genel şifreyi alıcılara göndermek için kaydederiz.

with open('acikanahtar.key', 'wb') as anahtar_dosyasi:
    anahtar_dosyasi.write(acikanahtar.save_pkcs1('PEM'))
    anahtar_dosyasi.close()

# SHA-256 ile özetliyoruz.

    mesaj = dosyayioku('mesaj')
    hash_mesaj = rsa.compute_hash(mesaj, 'SHA-256')

# Özetlenen mesajı özel anahtarlarla imzalayıp, imzalanan mesajı alıcıya göndermek için kaydediyoruz.

try:
    imza = rsa.sign_hash(hash_mesaj, gizlianahtar, 'SHA-256')
    d = open('imzalimesaj', 'wb')
    d.write(imza)
    print("İmzalama Başarıyla Tamamlandı.")

except:
    print("İmzalama Başarısız!")
