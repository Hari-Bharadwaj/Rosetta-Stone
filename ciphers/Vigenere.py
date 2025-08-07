def Vigenere_decoder(text,key):
    k,c,key,index='','',key.lower(),0
    for i in text:
        k_index=ord(key[index%len(key)])-ord('a')
        if i.isupper():
            c=chr((ord(i)-ord('A')-k_index+26)%26+ord('A'))
            index+=1
        elif i.islower():
            c=chr((ord(i)-ord('a')-k_index+26)%26+ord('a'))
            index+=1
        else:
            c=i
        k+=c
    return k

if __name__ == "__main__":
    text = input("Enter Text: ")
    key = input("Enter Key: ")
    print(Vigenere_decoder(text,key))
