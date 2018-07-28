#program to convert 12 hours to 24 hours format

def convertto24(time):
    if time[-2:]=="am" and time[:2]=="12":      #check last 2 elements are am and forst 2 elemets are 12
        return "00"+time[2:-2]
    elif time[-2:]=="am":                       #remove am
        return str1[:-2]
    elif time[-2:]=="pm" and time[:2]=="12":    #check last 2 elements are pm and forst 2 elemets are 12
        return time[:-2] 
    else:                                       #add 12 to hours and remove pm
        return str(int(time[:2])+12)+time[2:8]


print("enter time in 12 hour format as hh:mm:ss am/pm  """)
time=input("\ninput: ")
time.upper()
print("")
print("output:",convertto24(time),"hours")
