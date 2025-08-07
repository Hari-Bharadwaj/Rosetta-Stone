import string

all_alpha=list(string.ascii_uppercase)

def keyword_decoder(text,key):
    key,text=key.upper(),text.upper()
    key_new,ans=key,''
    for i in all_alpha:
        if i not in key:
            key_new+=i
    for i in range(len(text)):
        if text[i].isalpha():
            ans+=all_alpha[key_new.index(text[i])]
    return ans

if __name__=="__main__":
    print(keyword_decoder("EUUDN TIL EUUDN","Computer"))
