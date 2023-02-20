def main():
    eng = int(input("Would you like to encrypt(0) or decrypt(1)?\n"))
    msg = ""
    if eng == 0:
        msg = input("What would you like to encrypt?\n")
    elif eng == 1:
        msg = input("What would you like to decrypt?\n")
    else:
        quit
    
    # letters only! makealpha(key) helps generate lalpha/ralpha. 
    key1 = "HXUCZVAMDSLKPEFJRIGTWOBNYQ"
    key2 = "PTLNBQDEOYSFAVZKGJRIHWXUMC"
    
    

 #   print("L:", key1)
 #   print("R:", key2)
    print("I:", msg)
    print("O:", start(msg, key1, key2, eng), "\n")
    
    start(msg, key1, key2, eng, 1)


def start(msg, key1, key2, eng, show=0):
    msg = correct_case(msg)
    out = ""
    for L in msg:
        if eng == 0:
            key1, key2 = rotate_wheels(key1, key2, L)
            out += key1[0]
        else:
            key2, key1 = rotate_wheels(key2, key1, L)
            out += key2[0]
        key1, key2 = scramble(key1, key2)
        '''if show:
            print(key1, key2) '''           
    return out

def correct_case(string):
    return "".join([s.upper() for s in string if s.isalpha()])

def permu(alp, num):
    alp = alp[:num], alp[num:]
    return "".join(alp[::-1])

def rotate_wheels(key1, key2, key):
    newin = key2.index(key)
    return permu(key1, newin), permu(key2, newin) 

def scramble(key1, key2):
    key1 = list(key1)
    key1 = "".join([*key1[0],
                    *key1[2:14],
                    key1[1],
                    *key1[14:]])

    key2 = list(key2)
    key2 = "".join([*key2[0],
                    *key2[2:14],
                    key2[1],
                    *key2[14:]])
    return key1, key2

main()
