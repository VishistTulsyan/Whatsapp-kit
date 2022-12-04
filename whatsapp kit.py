print("HELLO EVERYONE\n"
      "THIS IS A WHATSAPP KIT DEVELOPED BY VISHIST TULSYAN")


def kit():
    import pywhatkit
    print("1. SEND SOMEONE A MSG\n"
          "2. SEND SOMEONE A MSG AT 12 A.M\n"
          "3. SEND A MSG TO A GROUP\n"
          "4. SEND A MSG TO GROUP AT 12 A.M\n"
          "5. SEND SOMEONE A MSG AT A SPECIFIC TIME\n"
          "6. SEND MSG TO A GROUP AT A SPECIFIC TIME\n")

    work = input("NOW SELECT WHAT YOU WANT TO DO")
    if work == "1":
        try:
            num = input("enter the number\n")
            msg = input("enter the msg you want to send\n")
            pywhatkit.sendwhatmsg_instantly(num, msg)
        except:
            print("an error occurred try again")
    elif work == "2":
        try:
            num = input("enter the number\n")
            msg = input("enter the msg you want to send\n")
            pywhatkit.sendwhatmsg(num, msg, 00, 00)
        except:
            print("an error occurred try again")
    elif work == "3":
        try:
            grp_name = input("enter the group name\n")
            msg = input("enter the msg you want to send\n")
            pywhatkit.sendwhatmsg_to_group_instantly(grp_name, msg)
        except:
            print("an error occurred try again")
    elif work == "4":
        try:
            grp_name = input("enter the group name\n")
            msg = input("enter the msg you want to send\n")
            pywhatkit.sendwhatmsg_to_group(grp_name, msg, 00, 00)
        except:
            print("an error occurred try again")
    elif work == "5":
        try:
            num = input("enter the number\n")
            msg = input("enter the msg you want to send\n")
            hr = int(input("enter the hour\n"))  # write the hour in 24 hrs format for ex write 8 pm as 20
            min = int(input("enter the min\n"))
            pywhatkit.sendwhatmsg(num, msg, hr, min)
        except:
            print("an error occurred try again")
    elif work == "6":
        try:
            grp_name = input("enter the group name\n")
            msg = input("enter the msg you want to send\n")
            hr = int(input("enter the hour\n"))  # write the hour in 24 hrs format for ex write 8 pm as 20
            min = int(input("enter the min\n"))
            pywhatkit.sendwhatmsg_to_group(grp_name, msg, hr, min)
        except:
            print("an error occurred try again")
    else:
        print("please enter between 1-6")


kit()


# code developed by Vishist Tulsyan

def res_nd_exit():
    print("do you want to restart again y/n")
    action = input()
    if action == "y":
        kit()
    else:
        print("okay, thanks for using my programme")


res_nd_exit()

code = 1

while code < 2:
    res_nd_exit()

# code developed by Vishist Tulsyan
# code developed by Vishist Tulsyan
# code developed by Vishist Tulsyan
# code developed by Vishist Tulsyan
