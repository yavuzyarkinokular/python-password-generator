import random
import time

karakter_secici = "qw2ert1yuıilkjh3gfdsazx4[^£cvbp5nm]?!€Q6WRTYUI7OP.MNB8VCXZ9SDFGHJK><"

while True:

    haneSayisi = int(input("Kaç haneli olması gerekiyor?\n"))

    sifre = ""
    for hane in range(0, haneSayisi):
        sifreUretici = random.choice(karakter_secici)
        sifre = sifre + sifreUretici
    print("Şifreniz= {} ".format(sifre))
    print("İyi günler dileriz..")
    # kullanıcı şifreyi kopyala yapıştır yapabilsin diye süre eklendi .
    time.sleep(5)
