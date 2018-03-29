import random

UpCase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ];
LowCase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o","p", "q", "r", "s", "t", "u", "v","w", "x"," y", "z"];
theNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

while True:
    i = 0
    newpassword = ""
    print("How many characters do you want your password to be?")
    length = int(input("Enter input here===>"))
    while(i < length):
        dice1 = random.randint(1,3)
        if dice1 == 1:
            newpassword += UpCase[random.randint(0,23)]
        elif dice1 == 2:
            newpassword += LowCase[random.randint(0,23)]
        else:
            newpassword += str(theNums[random.randint(0,9)])
        i+=1
    print("your new password is {}".format(newpassword))
    
        
