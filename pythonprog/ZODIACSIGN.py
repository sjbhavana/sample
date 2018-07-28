import string
date=int(input("Enter your date of Birth:  "))
month=str(input("enter the month: "))
if month=="december":
    astro="sagittarius" if (date<22) else "capricon"
elif month=="january":
    astro="capricon" if(date<20) else "aquarius"
elif month=="february":
    astro="aquarius" if(date<19) else "pisces"
elif month=="march":
    astro="pisces" if(date<21) else "aries"
elif month=="april":
    astro="aries" if(date<20) else "tarurus"
elif month=="may":
    astro="tarurus" if(date<21) else "gemini"
elif month=="june":
    astro="gemini" if(date<21) else "cancer"
elif month=="july":
    astro="cancer" if(date<21) else "leo"
elif month=="august":
    astro="leo" if(date<23) else "virgo"
elif month=="september":
    astro="virgo" if(date<20) else "libra"
elif month=="october":
    astro="libra" if(date<20) else "scorpion"
elif month=="november":
    astro="scorpion" if(date<20) else "sagittarius"
else:
    print("enter the valid date")
print("your zodiac sign is:", astro)
