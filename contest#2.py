parent = 0
while(parent<1):
    userVal = input("Enter the string...\n")
    enMeth = int(input("select the encryption type ...\n1 - Swapping by position  ...\n2 - Change position ...\n3 - Opposite switch ...\n"))
    while(True):
        if enMeth == 1:
            print("String after encyption ...")
            print(userVal[::-1])
            resp = input("enter y if you wish to decrypt otherwise press another key ...\n")
            if resp == 'y':
                print("String after decryption ...")
                print(userVal)
                ex = input("Enter 0 to continue of anyother number to exit ...")
                if ex == '0':
                    break
                else:
                    parent+=1
                    break
            else:
                break
        elif enMeth == 2:
            respA = int(input("By how many position to shift ..."))
            if len(userVal) < respA:
                print("Error ... shifiting value cannot be more than the length of the string ...")
            else:
                updVal = ''
                myList = list(userVal)
                for i in range(respA):
                    img = myList.pop()
                    myList.insert(0,img)
                for j in myList:
                    updVal +=j
                print("String after encryption ...")
                print(updVal)
                resp = input("enter y if you wish to decrypt otherwise press another key ...\n")
                if resp == 'y':
                    print("String after decryption ...")
                    print(userVal)
                    ex = input("Enter 0 to continue of anyother number to exit ...")
                    if ex == '0':
                        break
                    else:
                        parent+=1
                        break
                else:
                    break
        elif enMeth == 3:
            print('Opposite switch ...')
            myListi=[]
            updSt=''
            for i in userVal:
                imag = ord(i)
                myListi.append(chr(122-(imag-97)))
            for j in myListi:
                updSt +=j
            print('String after encryption ',updSt,'...')
            resp = input("enter y if you wish to decrypt otherwise press another key ...\n")
            if resp == 'y':
                print("String after decryption ...")
                print(userVal)
                ex = input("Enter 0 to continue of anyother number to exit ...")
                if ex == '0':
                    break
                else:
                    parent+=1
                    break
            else:
                break



    
        

        



