
lines = ""
#For easy2, key = 26 - 11 = 15
#For easy, key = 26 - 18 = 8
#For hard, key = 26 - 6 = 20
#For hard2, key = 26 - 23 = 3
EASY = "caesar_easy_encrypted.txt"
EASY2 = "caesar_easy_2_encrypted.txt"
HARD = "caesar_hard_encrypt.txt"
HARD2 = "caesar_hard_2_encrypt.txt"
#https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/
with open(HARD2) as f:
    lines = f.readlines()

line = lines[0]
line = line.lower()



for y in range(26):
    temp = ""
    for x in range(len(line)):
        letter = line[x]
        if letter.isalpha():
            temp += chr((ord(letter) + y - 97) % 26 + 97)
        else:
            temp += letter
    print(y)
    print(temp)
    print(" ")
    

    
    