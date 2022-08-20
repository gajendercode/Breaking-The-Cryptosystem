key = 'CRYPTANALYSIS'
mat = [['C','R','Y','P','T'],
               ['A','N','L','S','I'],
               ['B','D','E','F','G'],
               ['H','K','M','O','Q'],
               ['U','V','W','X','Z'],]

def play_fair(mat, cipher):
    for i in mat:
        if cipher[0] in i:
            row1 = mat.index(i)
            column1 = i.index(cipher[0])
    for i in mat:
        if cipher[1] in i:
            row2 = mat.index(i)
            column2 = i.index(cipher[1])
    
    #Case1: Same row
    if row1 == row2:
        if column1 == 0 and column2 != 0:
            cipher = mat[row1][4]+mat[row1][column2-1]
        elif column1 != 0 and column2 == 0:
            cipher = mat[row1][column1-1]+mat[row1][4]
        elif column1 == 0 and column2 == 0:
            cipher = mat[row1][4]+mat[row1][4]
        else:
            cipher = mat[row1][column1-1]+mat[row1][column2-1]
    
    #Case 2: Same columnumn
    elif column1 == column2:
        if row1 == 0 and row2 != 0:
            cipher = mat[4][column1]+mat[row2-1][column1]
        elif row1 != 0 and row2 == 0:
            cipher = mat[row1-1][column1]+mat[4][column1]
        elif row1 == 0 and row2 == 0:
            cipher = mat[4][column1]+mat[4][column1]
        else:
            cipher = mat[row1-1][column1]+mat[row2-1][column2]
            
    #Case3: Rectangle
    else:
        cipher = mat[row1][column2] + mat[row2][column1] 
    return cipher



cipher = 'DF ULYP XO CQD LFWC RUBHEDY, CQDYG LN XDYL EGIYIG LMP CQDYF.LYFNH HXPZ CQF YNILXKPB "NDCB_AN_BBHCN" PQ FQ CQPKZBK. OLC PMCUNUG YMB IPYDIDCQ OXY CMB LDZP AULHDFY. CX OALG RMB FWGI PMXBNTIP ZLSWS LFWFE PQ ZCYGY KIBAT XMNKI PMBYD.'
c_mo = cipher.replace(" ","").replace(",","").replace(".","").replace('"',"").replace("_","")
ans = ''
for i in range(0,len(c_mo),2):
    bigraph = c_mo[i]+c_mo[i+1]
    c_bi = play_fair(mat,bigraph)
    ans+=c_bi[0]+c_bi[1]

print(ans)
