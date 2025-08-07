def caesar_decoder(text, shift_value=1):
    k=''
    print('For shift value of:',shift_value)
    for i in text:
        if i.isupper():
            k+=chr(int((ord(i)-shift_value-ord('A'))%26)+ord('A'))
        elif i.islower():
            k+=chr(int((ord(i)-shift_value-ord('a'))%26)+ord('a'))
        elif i.isnumeric():
            k+=chr(int((ord(i)-shift_value-ord('0'))%10)+ord('0'))
        else:
            k+=i
    return k

def caesar_bruteforce(text):
    for i in range(0,25):
        print(caesar_decoder(text,i))
        
if __name__ == "__main__":
    text = input("Enter Text: ")
    caesar_bruteforce(text)
