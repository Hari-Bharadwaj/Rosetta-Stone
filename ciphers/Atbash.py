def Atbash_decoder(text):
    k=''
    for i in text:
        if i.isupper():
            k+=chr(ord('Z')+1+int('-'+str(1+(ord(i)%ord('A')))))
        elif i.islower():
            k+=chr(ord('z')+1+int('-'+str(1+(ord(i)%ord('a')))))
        elif i.isnumeric():
            k+=chr(ord('9')+1+int('-'+str(1+(ord(i)%ord('0')))))
        else:
            k+=i
    return k

if __name__ == "__main__":
    text = input("Enter text: ")
    print(Atbash_decoder(text))

