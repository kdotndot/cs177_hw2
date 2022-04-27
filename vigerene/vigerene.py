from cmath import inf

import string

EASY = "vigerene_easy_encrypted.txt"
MEDIUM = "vigerne_medium_encrypt.txt"
HARD = "vigerene_hard_encrypt.txt"



lines = ""
with open(HARD,encoding="utf8") as f:
    lines = f.readlines()


#For medium and hard
temp = ""
for x in lines:
    if "\n" in x:
        without_new_line = x.replace("\n", "")
    temp += without_new_line
lines[0] = temp

#Need line to be an array w a single string 
line = lines[0]
line = line.lower()


freq_in_english = {'a' : 8.15,
                   'b' : 1.44,
                   'c' : 2.76,
                   'd' : 3.79,
                   'e' : 13.11,
                   'f' : 2.92,
                   'g' : 1.99,
                   'h' : 5.26,
                   'i' : 6.35,
                   'j' : 0.13,
                   'k' : 0.42,
                   'l' : 3.39,
                   'm' : 2.54,
                   'n' : 7.10,
                   'o' : 8.00,
                   'p' : 1.98,
                   'q' : 0.12,
                   'r' : 6.83,
                   's' : 6.10,
                   't' : 10.47,
                   'u' : 2.46,
                   'v' : 0.92,
                   'w' : 1.54,
                   'x' : 0.17,
                   'y' : 1.98,
                   'z' : 0.08
                   }
ALPHABET = string.ascii_lowercase



def decryption(encrypt_letter, n):
    return chr((ord(encrypt_letter) - n - 97) % 26 + 97)



def IOC(freq, N):
    ioc = 0
    
    for x in freq:
        ioc += (freq[x] * (freq[x] - 1))/(N * (N-1))
    return ioc

def freq_find(sequence):
    N = len(sequence)
    freq = {}
    for x in sequence:
        if x not in freq:
            freq[x] = 1
        else:
            freq[x] += 1
    
    return freq, N
    
def chi_squared(freq, N):
    chi_squared = 0
    
    for x in range(0,len(ALPHABET)):
        letter = ALPHABET[x]
        if letter in freq: 
            chi_squared += pow(freq[letter] - (freq_in_english[letter] * N / 100) , 2) / ((freq_in_english[letter] * N / 100))
        
            
    return chi_squared


ans_sequences = []
#Finding key length 
for x in range(2, 20):
    #Finding letter frequencies
    sequences = []
    keylen = x
    for y in range(keylen):
        sequences.append([])
    count = 0
    #Go through the text and separate by 
    for y in range(len(line)):
        letter = line[y]
        if count >= keylen:
            count = 0
        if letter.isalpha():
            sequences[count].append(letter)    
            count += 1
    
    avg = 0
    for y in sequences:
        
        freq, N = freq_find(y)
        
        avg += IOC(freq, N)
        
    avg = avg / len(sequences)
    
    
    if x == 13:
        ans_sequences = sequences
    """ print(x)
    print(avg) """
    
    #Find out highest IOC = 5 or 10 for easy
    #9 for medium
    #13 for hard
    


    

ans = []
for x in ans_sequences:
    print(" ")
    temp = x
    min_chi = inf
    key = ""
    for y in range(0,len(ALPHABET)):
        decrypted = []
        for z in temp:
            decrypted.append(decryption(z, y + 1))
        freq, N = freq_find(decrypted)
        
        chi_square = chi_squared(freq, N)
        if chi_square < min_chi:
            min_chi = chi_square
            key = ALPHABET[y]
        print(ALPHABET[y] + " " + str(chi_square))
        
    
    ans.append(key)
    print(key)

print(ans)
        
        
#Key for easy = lewis
        
#Decryption

with open(HARD,encoding="utf8") as f:
    lines = f.readlines()
temp = ""
for x in lines:
    
    temp += x
lines[0] = temp
line = lines[0]
line = line.lower()


decrypted_text = ""
count = 0
for x in range(len(line)):
    letter = line[x]
    temp = ""
    if letter.isalpha():
        temp = decryption(letter,  1+ ALPHABET.index(ans[count]))
        decrypted_text += temp
        count += 1
        if count >= len(ans):
            count = 0
    else:
        decrypted_text += letter
print(decrypted_text)
            
            
                          
        
#Easy, key length 5, lewis, "the room displayed a modest and pleasant color-scheme, after one of the best standard designs of the decorator who “did the interiors” for most of the speculative-builders’ houses in zenith. the walls were gray, the woodwork white, the rug a serene blue; and very much like mahogany was the furniture—the bureau with its great clear mirror, mrs. babbitt’s dressing-table with toilet-articles of almost solid silver, the plain twin beds, between them a small table holding a standard electric bedside lamp, a glass for water, and a standard bedside book with colored illustrations—what particular book it was cannot be ascertained, since no one had ever opened it. the mattresses were firm but not hard, triumphant modern mattresses which had cost a great deal of money; the hot-water radiator was of exactly the proper scientific surface for the cubic contents of the room. the windows were large and easily opened, with the best catches and cords, and holland roller-shades guaranteed not to crack. it was a masterpiece among bedrooms, right out of cheerful modern houses for medium incomes. only it had nothing to do with the babbitts, nor with any one else. if people had ever lived and loved here, read thrillers at midnight and lain in beautiful indolence on a sunday morning, there were no signs of it. it had the air of being a very good room in a very good hotel. one expected the chambermaid to come in and make it ready for people who would stay but one night, go without looking back, and never think of it again."
    
        
   

    
        
    
        
    
        

    


            
                

            