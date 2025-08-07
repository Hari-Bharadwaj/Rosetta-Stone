import string


def matrix_gen(key):
    all_alpha=list(string.ascii_uppercase)
    key_new,mat=key.upper(),[]
    for i in all_alpha:
        if i not in key_new:
            if 'I' not in key_new and 'J' not in key_new:
                key_new+=i
            elif 'I' in key_new and i!='J':
                key_new+=i
            elif 'J' in key_new and i!='I':
                key_new+=i
    index=0
    for i in range(5):
        row_mat=[]
        for j in range(5):
            row_mat.append(key_new[index])
            index+=1
        mat.append(row_mat)
    #print(mat)
    return mat
            
def loc(a,b,matrix):
    x1,y1,x2,y2=0,0,0,0
    
    for i in range(5):
        for j in range(5):
            if a == 'J' and matrix[i][j] == 'I':
                x1,y1=i,j
            elif b=='J' and matrix[i][j] == 'I':
                x2,y2=i,j
            elif matrix[i][j]==a:
                x1,y1=i,j
            elif matrix[i][j]==b:
                x2,y2=i,j
    return x1,y1,x2,y2

def playfair_decoder(text,key):
    matrix=matrix_gen(key)
    text=text.replace(' ','').upper()
    res=''
    for i in range(0,len(text),2):
        x1,y1,x2,y2=loc(text[i],text[i+1],matrix)
        new_x1,new_y1,new_x2,new_y2=0,0,0,0
        if (x1==x2):
            if (y1-1)>=0 and (y2-1)>=0:
                new_x1,new_y1,new_x2,new_y2=x1,y1-1,x2,y2-1
            else:
                if (y1-1)<0 and (y2-1)>=0:
                    new_x1,new_y1,new_x2,new_y2=x1,4,x2,y2-1
                elif (y1-1)>=0 and (y2-1)<0:
                    new_x1,new_y1,new_x2,new_y2=x1,y1-1,x2,4
                else:
                    new_x1,new_y1,new_x2,new_y2=x1,4,x2,4
            #print("Same Row")
        elif (y1==y2):
            if (x1-1)>=0 and (x2-1)>=0:
                new_x1,new_y1,new_x2,new_y2=x1-1,y1,x2-1,y2
            else:
                if (x1-1)<0 and (x2-1)>=0:
                    new_x1,new_y1,new_x2,new_y2=4,y1,x2-1,y2
                elif (x1-1)>=0 and (x2-1)<0:
                    new_x1,new_y1,new_x2,new_y2=x1-1,y1,4,y2
                else:
                    new_x1,new_y1,new_x2,new_y2=4,y1,4,y2
            #print("Same Column")
        else:
            new_x1,new_y1,new_x2,new_y2=x1,y2,x2,y1
            #print("Rectangle")
        res+=(matrix[new_x1][new_y1]+matrix[new_x2][new_y2])
    return res



if __name__=="__main__":
    print(playfair_decoder("gatlmzclrqtx","Monarchy"))
