


lines = ""
with open('vigerene_easy_encrypted.txt') as f:
    lines = f.readlines()

line = lines[0]
line = line.lower()
print(line)

#Finding key length 
for x in range(2, 3):
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

    


            
                

            