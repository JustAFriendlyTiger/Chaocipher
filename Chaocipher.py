alphabet = "ABCDEFGHIJKLMNOPQRSTUZWXYZ"

pt = input("What would you like to encrypt?\n")
ct = ""

#The following is to verify that they inputted the text they want to encrypt
def verify():
    y_n = input("You have inputed:\n" + pt + "\nIs this correct? y/n \n")
    if y_n == "y":
        pass
    elif y_n == "n":
        pass
    else:
        pass
verify()

zenith = 1
nadir = 14
pos_2 = zenith + 1
pos_14 = nadir

#function to permute the left alphabet (ct alphabet)
def left_permute():
    ct_pos = zenith #ct_pos refers to the position of the ciphered text
    extract = zenith + 1

def extract():
    pass