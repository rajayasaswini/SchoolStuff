def checkCC(no):
    list = []
    for i in no:
        i = int(i)
        list.append(i)

    pointer = 0
    sumofm = []

    while pointer < len(list):
        sumofm.append(list[pointer]*2)
        pointer += 2

    for i in sumofm:
        c = str(i)
        if len(c) > 1:
            for j in c:
                rev_c = int(j)
                sumofm.append(rev_c)
            sumofm.remove(i)

    sum_m2 = 0

    for i in sumofm:
        sum_m2 += i

    pointer2 = 1

    while pointer2 <= len(list):
        sum_m2 += list[pointer2]
        pointer2 += 2

    sum_m2  = str(sum_m2)[::-1]

    if sum_m2[0] == '0':
        print("This credit card is valid!")
    else:
        print("This credit card is not valid!")
def import_no():
    filename = open(str(input("Enter the name of the file with the file type (e.g. .txt) at the end: ")))
    read_file = filename.read().split('\n')
    filename.close()
    for i in read_file:
        print (i)
        checkCC(i)
def generate():
    return 0
def get_num(ccnum):
    ccnum = ''
    for i in range(16):
        userentercc = int(input("Enter one number at a time. Enter the number from you credit card number: "))
        userentercc = str(userentercc)
        ccnum += userentercc
    return ccnum
def quit():
    return 0
usermenuinp = ''
def menu():
    print("1. Check my Card","2. Import numbers to check","3. Generate a valid credit card number","4. Quit")
    try:
        usermenuinp = int(input("Enter a number to select an option from the menu: "))
    except:
        print("Please enter a number: ")
    else:
        while usermenuinp < 0 or usermenuinp > 4:
            usermenuinp = int(input("Enter a number from 1-4 to select an option from the menu: "))
    return usermenuinp
menu()

cc_num = ''
while usermenuinp != 4:
    if usermenuinp == 1:
        get_num(cc_num)
        checkCC(cc_num)
        menu()
    elif usermenuinp == 2:
        import_no()
        menu()
    elif usermenuinp == 3:
        generate()
        menu()
