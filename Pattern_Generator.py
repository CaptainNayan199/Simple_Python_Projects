num = int(input("Give me a number to design a patter : "))
patt = (input("Thanks, Now illustrate desired pattern (`*` or `#` or `$`) : "))
if (patt=='star') or (patt=='Star') or (patt=='STAR') or (patt=='*'):
    k=1
    for i in range(0, num):
        for j in range(0, k):
            print("* ", end="")
        k = k + 1
        print()
elif (patt=='hash') or (patt=='Hash') or (patt=='HASH') or (patt=='#'):
    k=1
    for i in range(0, num):
        for j in range(0, k):
            print("# ", end="")
        k = k + 1
        print()
elif (patt=='dollar') or (patt=='Dollar') or (patt=='DOLLAR')  or (patt=='$'):
    k=1
    for i in range(0, num):
        for j in range(0, k):
            print("$ ", end="")
        k = k + 1
        print()
else:
    print("Please provide some valid pattern style, be responsbile mg!!!")