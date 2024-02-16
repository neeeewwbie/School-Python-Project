from datetime import datetime, timedelta
time = datetime.now()
import random
horoscope = ['This is a day when any problems that have been bothering you can be completely resolved. There are many people who help you, and many who take your side when there are disagreements.','It is a day when you feel depressed. It is a time when you meet a lot of new people, but you do not feel refreshed. In order to be understood, you need to have a more open mind.','Things that seem strange It is a day where you can laugh and laugh about what is going on around here. If you have been hurt by someone, you may receive a hand of reconciliation from that person.','Unusually grumpy. This is a day when the situation gets worse and the sense of victimization grows. It is not that I have a lot of work or that my body is tired, but I am a bit bored and bored, so I become more mischievous and often get irritated by people around me.','It is a day when you will find luck in unexpected places. If you have an ear for words, you may end up becoming the envy of those around you. You may get lucky in a place you visit for the first time.','It is a day when I feel strangely tired, perhaps because of the weather or because of dream of previous day. I even feel sleepy, as if it is the beginning of spring. Sometimes it is good to move your body to relieve fatigue.','Accidental meetings This is a day when accidental incidents and accidents become frequent. This does not pose a huge risk, but you may feel a little embarrassed. Although it can be stressful, this tension can actually be beneficial.','bothering you It will be a peaceful day without work. It is not a time of great luck, but it is time to do the basics no matter what you do. If there is something you have been thinking about pursuing, do not delay.','This is a day when you feel better. In particular, if you have been feeling a little less confident and intimidated, you will feel completely different tomorrow. It will be a day full of morale.','This is the day when you get to know a friend who is different from the people you have met so far. At first, it may be awkward because of the unfamiliar atmosphere of the other person, but suddenly you can become very close.','It is a day when strange incidents often occur. You may also be criticized by others even though it is not your fault. Rather than asserting your legitimacy, try to give in and find a compromise.​​​​​​​​','It is a day when I get to spend some free time for a long time. If you have been bothered by a lot of things, you will now be able to let go. It is also a day when you can solve problems without putting in a lot of effort.']
lucky_time = ['12 AM','1 AM','2 AM','3 AM','4 AM','5 AM','6 AM','7 AM','8 AM','9 AM','10 AM','11 AM','12 PM','1 PM','2 PM','3 PM','4 PM', '5 PM','6 PM','7 PM','8 PM','9 PM','10 PM','11 PM']
lucky_item = ['Tumbler','Music','Aroma Goods','Perfume','Lip Gloss, Lip stick','Gift','Mirror','Book','Flower','Delivery','Lottery']
lucky_place = ['Fast food restaurant','Cafe','Bar','Pension, Resort','Convenience Store','Camping Site','Hair Salon','Restaurant','Shopping Mall','Public Transportation']
lucky_color = ['Red','Orange','Yellow','Green','Blue','Navy','Violet','Brown','White','Black','Light Green','Light Blue','Pink','Grey']
a = random.choice(horoscope)
b = random.choice(lucky_time)
c = random.choice(lucky_item)
d = random.choice(lucky_place)
e = random.choice(lucky_color)

name = input("Your name:")
birthday = int(input("Your birthday(month date only number without space ex. 0101): "))
if birthday <= 119:
    Zodiac = 'Capricornus'
    print(f"name : {name}")
    print(f"birthday(month + day) : {birthday}")
    print(f"your Zodiac : {Zodiac}")
    print("date :", time.date())
    print(f"horoscope : {a}")
    print("lucky tips:")
    print(f"lucky time : {b}")
    print(f"lucky item : {c}")
    print(f"lucky place : {d}")
    print(f"lucky color : {e}")
elif 120 <= birthday <=  218:
    Zodiac = 'Aquarius'
    print(f"name : {name}")
    print(f"birthday(month + day) : {birthday}")
    print(f"your Zodiac : {Zodiac}")
    print("date :", time.date())
    print(f"horoscope : {a}")
    print("lucky tips:")
    print(f"lucky time : {b}")
    print(f"lucky item : {c}")
    print(f"lucky place : {d}")
    print(f"lucky color : {e}")
elif 219 <= birthday <= 320:
    Zodiac = 'Pisces'
    print(f"name : {name}")
    print(f"birthday(month + day) : {birthday}")
    print(f"your Zodiac : {Zodiac}")
    print("date :", time.date())
    print(f"horoscope : {a}")
    print("lucky tips:")
    print(f"lucky time : {b}")
    print(f"lucky item : {c}")
    print(f"lucky place : {d}")
    print(f"lucky color : {e}")
elif 321 <= birthday <= 419:
    Zodiac = 'Aries'
    print(f"name : {name}")
    print(f"birthday(month + day) : {birthday}")
    print(f"your Zodiac : {Zodiac}")
    print("date :", time.date())
    print(f"horoscope : {a}")
    print("lucky tips:")
    print(f"lucky time : {b}")
    print(f"lucky item : {c}")
    print(f"lucky place : {d}")
    print(f"lucky color : {e}")
elif 420 <= birthday <= 520:
    Zodiac = 'Taurus'
    print(f"name : {name}")
    print(f"birthday(month + day) : {birthday}")
    print(f"your Zodiac : {Zodiac}")
    print("date :", time.date())
    print(f"horoscope : {a}")
    print("lucky tips:")
    print(f"lucky time : {b}")
    print(f"lucky item : {c}")
    print(f"lucky place : {d}")
    print(f"lucky color : {e}")
elif 521 <= birthday <= 621:
    Zodiac = 'Gemini'
    print(f"name : {name}")
    print(f"birthday(month + day) : {birthday}")
    print(f"your Zodiac : {Zodiac}")
    print("date :", time.date())
    print(f"horoscope : {a}")
    print("lucky tips:")
    print(f"lucky time : {b}")
    print(f"lucky item : {c}")
    print(f"lucky place : {d}")
    print(f"lucky color : {e}")
elif 622 <= birthday <= 722:
    Zodiac = 'Cancer'
    print(f"name : {name}")
    print(f"birthday(month + day) : {birthday}")
    print(f"your Zodiac : {Zodiac}")
    print("date :", time.date())
    print(f"horoscope : {a}")
    print("lucky tips:")
    print(f"lucky time : {b}")
    print(f"lucky item : {c}")
    print(f"lucky place : {d}")
    print(f"lucky color : {e}")
elif 723 <= birthday <= 822:
    Zodiac = 'Leo'
    print(f"name : {name}")
    print(f"birthday(month + day) : {birthday}")
    print(f"your Zodiac : {Zodiac}")
    print("date :", time.date())
    print(f"horoscope : {a}")
    print("lucky tips:")
    print(f"lucky time : {b}")
    print(f"lucky item : {c}")
    print(f"lucky place : {d}")
    print(f"lucky color : {e}")
elif 823 <= birthday <= 922:
    Zodiac = 'Virgo'
    print(f"name : {name}")
    print(f"birthday(month + day) : {birthday}")
    print(f"your Zodiac : {Zodiac}")
    print("date :", time.date())
    print(f"horoscope : {a}")
    print("lucky tips:")
    print(f"lucky time : {b}")
    print(f"lucky item : {c}")
    print(f"lucky place : {d}")
    print(f"lucky color : {e}")
elif 923 <= birthday <= 1023:
    Zodiac = 'Libra'
    print(f"name : {name}")
    print(f"birthday(month + day) : {birthday}")
    print(f"your Zodiac : {Zodiac}")
    print("date :", time.date())
    print(f"horoscope : {a}")
    print("lucky tips:")
    print(f"lucky time : {b}")
    print(f"lucky item : {c}")
    print(f"lucky place : {d}")
    print(f"lucky color : {e}")
elif 1024 <= birthday <= 1121:
    Zodiac = 'Scorpius'
    print(f"name : {name}")
    print(f"birthday(month + day) : {birthday}")
    print(f"your Zodiac : {Zodiac}")
    print("date :", time.date())
    print(f"horoscope : {a}")
    print("lucky tips:")
    print(f"lucky time : {b}")
    print(f"lucky item : {c}")
    print(f"lucky place : {d}")
    print(f"lucky color : {e}")
elif 1122 <= birthday <= 1221:
    Zodiac = 'Sagittarius'
    print(f"name : {name}")
    print(f"birthday(month + day) : {birthday}")
    print(f"your Zodiac : {Zodiac}")
    print(f"horoscope : {a}")
    print("lucky tips:")
    print(f"lucky time : {b}")
    print(f"lucky item : {c}")
    print(f"lucky place : {d}")
    print(f"lucky color : {e}")
    print("date :", time.date())
elif 1222 <= birthday <= 1231:
    Zodiac = 'Capricornus'
    print(f"name : {name}")
    print(f"birthday(month + day) : {birthday}")
    print(f"your Zodiac : {Zodiac}")
    print(f"horoscope : {a}")
    print("lucky tips:")
    print(f"lucky time : {b}")
    print(f"lucky item : {c}")
    print(f"lucky place : {d}")
    print(f"lucky color : {e}")
    print("date :", time.date())
else:
    Zodiac = 'Error'
    print(f"{Zodiac} has been occured, please input correct value")
