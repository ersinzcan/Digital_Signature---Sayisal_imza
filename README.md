1.SAYISAL İMZA NEDİR?

Sayısal İmza - bir tür elektronik imza - bir mesajın (örneğin, bir e-posta, bir kredi kartı işlemi veya bir dijital belge) gerçekliğini ve bütünlüğünü doğrulamak için
rutin olarak kullanılan matematiksel bir algoritmadır. Sayısal imzalar, bir kişiye veya varlığa özgü sanal bir parmak izi oluşturur ve kullanıcıları tanımlamak ve
dijital mesajlar veya belgelerdeki bilgileri korumak için kullanılır. E-postalarda, e-posta içeriğinin kendisi sayısal imzanın bir parçası haline gelir. Sayısal imzalar,
diğer elektronik imza biçimlerinden önemli ölçüde daha güvenlidir.


1.1 SAYISAL İMZA OLUŞTURMA VE DOĞRULAMA ADIMLARI

![image](https://user-images.githubusercontent.com/81472780/206850524-33e7d75c-a0e4-4e20-ad86-a94c54d8b6e5.png)


2.İMZALAMA

2.1 RSA İLE ANAHTAR OLUŞTURMA

  Bu projede RSA kullanılmıştır. RSA algoritması kullanılarak özel anahtar ve genel anahtar olmak üzere iki adet anahtar oluşturulur ve bu oluşturulan anahtarlardan
genel olanı herkesle paylaşılabilir ancak özel anahtar belgeleri imzalamak için kullanıldığı için kimseyle paylaşılmaz

2.2 MESAJIN ÖZETLENMESİ

  Mesajı  özetlenmek için SHA256 kullandık. Özetleme tek taraflı yapılan bir işlemdir özetten asıl mesaja dönülemez ancak mesaj üzerinde yapılan değişiklikler
özetlerin karşılaştırılmasıyla anlaşılabilir. 

2.3 İMZALAMA

  Özetlenen mesaj ve özel anahtar birlikte kullanılarak yeni bir imza mesajı oluşturulur bu oluşturulan imza  mesajı ve mesaj karşı tarafa iletilir. 

2.4 DOĞRULAMA

  İmzalı gelen veri genel anahtarla açılır mesajların özetleri birbirleriyle karşılaştırılır. Doğrulama işlemi sonunda belgenin doğrulanıp doğrulanmadığı döndürülür. 
