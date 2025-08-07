import math
def columnar_decoder(text,key):
    text,index=text.replace(' ',''),0
    row_len=int(math.ceil(len(text)/len(key)))
    key_sorted="".join(sorted(key))

    cipher_dict={}
    for i in key_sorted:
        row=''
        for j in range(row_len):
            row+=text[index]
            index+=1
        cipher_dict[i]=row

    res,c=[],0
    for i in range(len(key)):
        res.append([])

    for i in key:
        res[c]+=cipher_dict[i]
        c+=1

    ans=''
    for i in range(row_len):
        for j in range(len(key)):
            ans+=res[j][i]
    return ans
            
if __name__=="__main__":
    print(columnar_decoder("EVUACDESERORDENWIR","ZEBRAS"))
