def aminus(a):
    for i in range(26):
        if (a * i) % 26 == 1:
            return i
    return None

def affine_decoder(text, a=1, b=1):
    a_inv = aminus(a)
    if a_inv is None:
        return None
    k = ''
    for i in text:
        if i.isupper():
            x = ord(i) - ord('A')
            k += chr(((a_inv * (x - b)) % 26) + ord('A'))
        elif i.islower():
            x = ord(i) - ord('a')
            k += chr(((a_inv * (x - b)) % 26) + ord('a'))
        else:
            k += i
    return k

def affine_bruteforce(text):
    a_dict=[1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    for i in a_dict:
        for j in range(1,27):
            print("For a=",i,"and b=",j,"The decrypted text is:",affine_decoder(text,i,j))
if __name__ == "__main__":
    text=input("Enter the Text:")#"UBBAHK CAPJKX"
    #a=int(input("Enter a value:"))
    #b=int(input("Enter b value:"))
    #print(affine_decoder(text, a, b))
    affine_bruteforce(text)
