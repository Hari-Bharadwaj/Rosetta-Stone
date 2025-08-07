def rail_decoder(text,key):
    text=text.replace(' ','')
    row,col,direction,cipher_dict=0,0,0,[]
    for i in range(key):
        row_dict=[]
        for j in range(len(text)):
            row_dict.append('')
        cipher_dict.append(row_dict)
    
    for i in range(len(text)):
        cipher_dict[row][col]='*'
        if direction==0:
            if row!=key-1:
                row+=1
            else:
                row-=1
                direction=1
        else:
            if row!=0:
                row-=1
            else:
                row+=1
                direction=0
        col+=1
    index=0
    for i in range(key):
        for j in range(len(text)):
            if cipher_dict[i][j] == '*' and index < len(text):
                cipher_dict[i][j]=text[index]
                index+=1
    dec=''
    for i in range(len(text)):
        for j in range(key):
            if cipher_dict[j][i]!='':
                dec+=cipher_dict[j][i]
    return dec
            

if __name__=="__main__":
    print(rail_decoder("WECRUO ERDSOEERNTNE AIVDAC",3))
