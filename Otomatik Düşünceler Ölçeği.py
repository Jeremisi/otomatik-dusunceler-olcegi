print("Aşağıda kişilerin zaman zaman aklına gelen bazı düşünceler sıralanmıştır. Lütfen her birini okuyarak, bu düşüncelerin SON BİR HAFTA içinde aklınızdan ne kadar sıklıkla geçtiğini işaretleyiz. Lütfen her bir maddeyi dikkatle okuyunuz  ve maddelerin yanındaki uygun sayıyı aşağıdaki şıkları dikkate alarak işaretleyiniz.")

print("Hiç aklımdan geçmedi: 1")
print("Ender olarak aklımdan geçti: 2")
print("Arada sırada aklımdan geçti: 3")
print("Sık sık aklımdam geçti: 4")
print("Hep aklımdan geçti: 5")


print("Tüm dünya bana karşıymış gibi geliyor")
x1 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Hiçbir işe yaramıyorum")
x2 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Neden hiç başarılı olamıyorum")
x3 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Beni hiç kimse anlamıyor")
x4 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Başkalarını düş kırıklığına uğrattığım oldu")
x5 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Devam edebileceğimi sanmıyorum")
x6 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Keşke daha iyi bir insan olsaydım")
x7 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Öyle güçsüzüm ki ...")
x8 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Hayatım istediğim gibi gitmiyor")
x9 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Kendimi düş kırıklığına uğrattım")
x10 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Artık hiçbir şeyin tadı kalmadı")
x11 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Artık dayanamayacağım")
x12 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Bir türlü harekete geçemiyorum")
x13 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Neyim var benim")
x14 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Keşke başka bir yerde olsaydım")
x15 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Hiçbir şeyin iki ucunu bir araya getiremiyorum")
x16 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Kendimden nefret ediyorum")
x17 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Değersiz bir insanım")
x18 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Keşke birden yok olabilseydim")
x19 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Ne zorum var benim")
x20 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Hayatta hep kaybetmeye mahkûmum")
x21 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Hayatım karmakarışık")
x22 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Başarısızım")
x23 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Hiçbir zaman başaramayacağım")
x24 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Kendimi çok çaresiz hissediyorum")
x25 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Bir şeylerin değişmesi gerek")
x26 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Bende mutlaka bir bozukluk olmalı")
x27 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Geleceğim kasvetli")
x28 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Hiçbir şey için uğraşmaya değmez")
x29 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))

print("Hiçbir şeyi bitiremiyorum")
x30 = int(input("Ne kadar sıklıkla aklınızdan geçti: "))



x = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30]

x = sum(x)

#SONUÇ (RESULT)

print(f"Toplam puanınız {x}.")

if 30 > x:
    print("Testiniz geçersiz. Yanıtlarınızı kontrol ediniz.")
elif 30<= x <90:
    print("Otomatik düşünceleriniz ortalama puandan daha düşük")
elif 90 <= x < 150:
    print("Otomatik düşünceleriniz ortalama puandan daha fazla")
else:
    print("Testiniz geçersiz. Yanıtlarınızı kontrol ediniz.")



