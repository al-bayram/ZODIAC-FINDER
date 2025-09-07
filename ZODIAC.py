print('----------------------------')
print("HALOO!!, ZODIAC FINDER HE'RE")
print('----------------------------')
print('Kamu bisa mengetahui Zodiac yang kamu miliki beserta kepribadiannya')
print('---------------------------------------------------------')
day = int(input("Silahkan masukkan tanggal lahir Anda (1-31): "))
print('---------------------------------------------------------')
month = int(input("Silahkan masukkan bulan lahir Anda (1-12): "))
if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        print ("Zodiac kamu adalah Aquarius!")
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        print ("Zodiac kamu adalah Pisces!")
elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        print ("Zodiac kamu adalah Aries!")
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        print ("Zodiac kamu adalah Taurus!")
elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        print ("Zodiac kamu adalah Gemini!")
elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        print ("Zodiac kamu adalah Cancer!")
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        print ("Zodiac kamu adalah Leo!")
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        print ("Zodiac kamu adalah Virgo!")
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        print ("Zodiac kamu adalah Libra!")
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        print ("Zodiac kamu adalah Scorpio!")
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        print ("Zodiac kamu adalah Sagittarius!")
elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        print ("Zodiac kamu adalah Capricorn!")
else:
    print('Tanggal Dan Bulan Lahir Tidak Valid ')

print('---------------------------------------------------------')
print('Kamu telah mengetahui Zodiac pada diri kamu')
memori = input('Apakah kamu mau mengetahui kepribadianmu berdasarkan Zodiac kamu?(Jawab ya/tidak)').lower()
print('---------------------------------------------------------')
if memori == 'ya':
        zodiac = input('Pilihan Bagus!, Masukkan Zodiac kamu dan kamu akan mengetahui kepribadianmu.')       
        if zodiac == "Aquarius":
                print("Aquarius dikenal sebagai orang yang inovatif, independen, dan berpikiran terbuka. Mereka sering kali memiliki pemikiran yang unik dan suka membantu orang lain.")
        elif zodiac == "Pisces":
                print("Pisces adalah orang yang sensitif, intuitif, dan penuh empati. Mereka sering kali memiliki imajinasi yang kaya dan suka berkhayal.")
        elif zodiac == "Aries":
                print("Aries dikenal sebagai pemimpin yang berani, penuh semangat, dan kompetitif. Mereka suka tantangan dan tidak takut untuk mengambil risiko.")
        elif zodiac == "Taurus":
                print("Taurus adalah orang yang stabil, praktis, dan menyukai kenyamanan. Mereka menghargai keindahan dan sering kali memiliki selera yang baik.")
        elif zodiac == "Gemini":
                print("Gemini dikenal sebagai komunikator yang cerdas, fleksibel, dan penuh rasa ingin tahu. Mereka suka bergaul dan memiliki banyak teman.")
        elif zodiac == "Cancer":
                print("Cancer adalah orang yang emosional, intuitif, dan peduli. Mereka sangat setia kepada orang-orang terdekat dan suka menciptakan suasana yang nyaman.")
        elif zodiac == "Leo":
                print("Leo dikenal sebagai orang yang percaya diri, karismatik, dan penuh semangat. Mereka suka menjadi pusat perhatian dan memiliki jiwa kepemimpinan.")
        elif zodiac == "Virgo":
                print("Virgo adalah orang yang analitis, teliti, dan praktis. Mereka suka membantu orang lain dan sering kali memiliki perhatian terhadap detail.")
        elif zodiac == "Libra":
                print("Libra dikenal sebagai orang yang adil, diplomatis, dan menyukai keindahan. Mereka sering kali mencari keseimbangan dalam hidup.")
        elif zodiac == "Scorpio":
                print("Scorpio adalah orang yang intens, misterius, dan penuh gairah. Mereka memiliki kedalaman emosional yang kuat dan sangat setia.")
        elif zodiac == "Sagittarius":
                print("Sagittarius dikenal sebagai petualang, optimis, dan suka kebebasan. Mereka suka menjelajahi hal-hal baru dan memiliki pandangan yang luas.")
        elif zodiac == "Capricorn":
                print("Capricorn adalah orang yang disiplin, ambisius, dan bertanggung jawab. Mereka memiliki tujuan yang jelas dan bekerja keras untuk mencapainya.")
        else:
                print('Coba ulangi dengan awalan huruf kapital!, atau mungkin Zodiac mu tidak eksis?')
elif memori == 'tidak':
        print('Baiklah,tapi mungkin kamu akan menyesali ini :p')
elif memori !='ya' or memori != 'tidak':
        print('Zodiac macam apa ini!!??')

