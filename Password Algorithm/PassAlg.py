from time import sleep
import os
import math
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Password Algorithm by RedBall")

a = 'a'
b = 'b'
c = 'c'
alphabets ='abcdefghijklmnopqrstuvwxyz'
alphabets_caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def code():

    Options = input(str("""What would you like to? \
    a.) Make a new password \
    b.) Find a password \
    c.) Credits : """))

    while Options == a:
        website_name = input(str("Name of Website: "))
        number = input(str("Favorite Number: "))
        name = input(str("Your first name: "))
        s = input(str("Pick a number from 1-26: "))
        four_digits = input(str("What is the last 4 digits of your phone number: "))

        n = len(website_name)

        output = ""

        for i in range(n):
            character = website_name[i]
            location = alphabets.find(character)
            new_location = (location + 3) % 26
            output += alphabets[new_location]

        #print(output)

        numint = int(number)
        newnum1 = numint - (numint * 2)

        #print(newnum1)

        newnum2 = numint * 5

        #print(newnum2)

        
        caps = name.upper()

        reversed_caps =''.join(reversed(caps))
        
        ss = int(s)
        nn = len(reversed_caps)

        output1 = ""

        for i in range(nn):
            character = reversed_caps[i]
            location = alphabets_caps.find(character)
            new_location = (location + ss) % 26
            output1 += alphabets_caps[new_location]
        
        #print(output1)

        symbol = four_digits.replace("0", ")").replace("1", "!").replace("2", "@").replace("3", "#").replace("4", "$").replace("5", "%").replace("6", "^").replace("7", "&").replace("8", "*").replace("9", "(")

        #print(symbol)

        str_output1 = str(output1)
        str_newnum1 = str(newnum1)
        str_symbol = str(symbol)
        str_output = str(output)
        str_newnum2 = str(newnum2)




        password = str_output1 + str_newnum1 + str_symbol + str_output + str_newnum2

        print(str('Your password is:'), password)
        password_name = input(str("Name your password: "))
        sleep(2)
        print("Saving Password")
        file_write = open(password_name + ".txt","w+")
        file_write.write(password)
        file_write.close()
        sleep(1.5)
        print("Password Saved!")
        sleep(2)
        os.system('cls')
        code()

    while Options == b:
        file_name = input(str("Name of Password: "))
        File_object = open(file_name + ".txt","r")
        File_read = File_object.read()
        print("Your password is:" + File_read)
        sleep(2)
        file_continue = input(str("Press enter to continue: "))
        os.system('cls')
        code()


    while Options == c:
        print("This was made by RedBall. Support means a lot. Thank you!")
        sleep(6)
        os.system('cls')
        code()


    else:
        print("Command not Found!")
        sleep(2)
        os.system('cls')
        code()

code()
