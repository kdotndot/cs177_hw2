from cmath import inf
import string

EASY = "mono_easy_encrypt.txt"
MEDIUM = "mono_medium_encrypt.txt"
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
def split(word):
    return [char for char in word]

ALPHABET = split(ALPHABET)
#Removing known transformations
ALPHABET.remove("f")
ALPHABET.remove("e")
ALPHABET.remove("i")
ALPHABET.remove("l")
ALPHABET.remove("v")
ALPHABET.remove("g")
ALPHABET.remove("h")
ALPHABET.remove("r")
ALPHABET.remove("s")
ALPHABET.remove("d")
ALPHABET.remove("y")
ALPHABET.remove("m")
ALPHABET.remove("c")
ALPHABET.remove("w")
ALPHABET.remove("p")
ALPHABET.remove("t")
ALPHABET.remove("n")
ALPHABET.remove("u")
ALPHABET.remove("k")
ALPHABET.remove("z")


def freq_find(sequence):
    freq = {}
    N = 0
    for x in sequence:
        if x.isalpha():
            if x not in freq:
                freq[x] = 1
            else:
                freq[x] += 1
            N += 1
    
    return freq, N

def chi_squared(freq, N):
    chi_squared = 0
    
    for x in range(0,len(ALPHABET)):
        letter = ALPHABET[x]
        if letter in freq: 
            chi_squared += pow(freq[letter] - (freq_in_english[letter] * N / 100) , 2) / ((freq_in_english[letter] * N / 100))
        
    return chi_squared


lines = ""
with open(EASY,encoding="utf8") as f:
    lines = f.readlines()


#Simple txt parsing
temp = ""
for x in lines:
    if "\n" in x:
        without_new_line = x.replace("\n", "")
    temp += without_new_line
lines[0] = temp
line = lines[0]
line = line.lower()
freq, N = freq_find(line)
freq["v"] = 0
N += 1

#Removing known transformations
freq.pop("u")
freq.pop("b")
freq.pop("l")
freq.pop("j")
freq.pop("c")
freq.pop("n")
freq.pop("x")
freq.pop("g")
freq.pop("f")
freq.pop("r")
freq.pop("d")
freq.pop("t")
freq.pop("o")
freq.pop("a")
freq.pop("q")
freq.pop("k")
freq.pop("i")
freq.pop("w")
freq.pop("m")
freq.pop("e")





#Comparing english letter frequencies and picking highest chi_squared value
ans = {}

for x in freq:
    min_chi = inf
    key = ""
    print(x)
    
    for y in range(0,len(ALPHABET)):
        chi_square = pow(freq[x] - (freq_in_english[ALPHABET[y]] * N / 100) , 2)
        if chi_square < min_chi:
            min_chi = chi_square
            key = ALPHABET[y]
    print("ALPHABET IS " + str(ALPHABET))
    ans[x] = key    
    ALPHABET.remove(key)
    print("")




ans["u"] = "f"
ans["b"] = "e"
ans["l"] = "i"
ans["j"] = "l"
ans["c"] = "v"
ans["n"] = "g"
ans["x"] = "h"
ans["g"] = "r"
ans["f"] = "s"
ans["r"] = "d"
ans["d"] = "y"
ans["t"] = "m"
ans["o"] = "c"
ans["a"] = "w"
ans["q"] = "p"
ans["k"] = "t"
ans["i"] = "n"
ans["w"] = "u"

ans["m"] = "k"
ans["e"] = "z"

print(ans)

#Decryption
#U = F, B = E, U = T, J = L, C = V, N = G, X = H, G = R, F = S

with open(EASY,encoding="utf8") as f:
    lines = f.readlines()
temp = ""
for x in lines:
    temp += x
lines[0] = temp
line = lines[0]
line = line.lower()


decrypted_text = ""

for x in range(len(line)):
    letter = line[x]
    temp = ""
    if letter.isalpha():  
        temp = ans[letter]
        decrypted_text += temp
    else:
        decrypted_text += letter
print(decrypted_text)

