name = input("Give me a secret and single word to encode : ")
length = len(name)
if length >= 3:
    first_char = name[0]
    name = name[1:]
    name = name + first_char
    ran_first = input("Give me a 3 character long random word : ")
    ran_last = input("Give me a 3 character long random word : ")
    dec_name = ran_first+name+ran_last
    print(f"Your encoded secret word is `{dec_name}`.")
    ask = input("Do you want to decode your secret word ? [Y/N] : ")
    if ask == 'y' or ask == 'Y' or ask == "yes" or ask == 'YES' or ask =="Yes":
        print("I am decoding it...... Here it is")
        ec_name = dec_name[3:-3]
        l_index = ec_name[len(ec_name)-1]
        ec_name = ec_name[0:-1]
        ec_name = l_index+ec_name
        print(f"Your decoded and original secret word is `{ec_name}`")
    else:
        print("If you dont wanna decode it then fine... It's your choice. Bye have a good time.")


elif length>=2 and length<3:
    dec_rev = ""
    for i in name:
        dec_rev = i + dec_rev
    print(
        f"Hmmm! You gave a 2 character long secret word, so i will just reverse it and present you as `{dec_rev}`")
    ask = input("Do you want to decode your secret word ? [Y/N] : ")
    if ask == 'y' or ask == 'Y' or ask == "yes" or ask == 'YES' or ask =="Yes":
        print("I am decoding it...... Here it is")
        ec_rev = ""
        for i in dec_rev:
            ec_rev = i + ec_rev
        print(f"Your encoded and original secret word is `{ec_rev}`")
    else:
        print("If you dont wanna encode it then fine... It's your choice. Bye have a good time.")

else:
    print("I am sorry but i cannot decode and encode for a single character or multi word. Better if you give me multi character and single word (eg: aeroplane)")
