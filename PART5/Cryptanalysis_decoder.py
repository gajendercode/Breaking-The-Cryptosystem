#!/usr/bin/env python
# coding: utf-8

# In[2]:

import numpy as np
from pyfinite import ffield


# In[3]:

def square(a, b):
    return (a*a, b*b)

processed=[]
with open("ciphertexts.txt",'r') as f:
    for line in f.readlines():
        x = line.split()
        processed.extend(x)
    
    
with open("ciphertexts.txt",'w+') as file:
    i = 0
    new_text = ""
    for word in processed:
        if(i!=0 and i%128==0):
            file.write(new_text.strip())
            new_text = ""
            file.write('\n')
        new_text+=word
        new_text+=' '
        i+=1
    file.write(new_text.strip())

F = ffield.FField(7, gen=0x83, useLUT=-1)

expo = []
i=0
while i <128:
    expo.append([-1]*128)
    i+=1




# In[5]:


#functions for Field elements
def summation(p1, num2):
 return p1^num2


# In[6]:


def Product(x, y):
  a = F.Multiply(x,y)
  tempo=a
  b= tempo
  return b


def PowerUp(base, power):
    if(expo[base][power]!=-1):
        return expo[base][power]


    result = 0
    if(power==1):
        result = base
    if(power==0):
        result = 1

    elif(power%2 != 1):
        result = Product(PowerUp(base,power//2), PowerUp(base,power//2))
        
    else:
        sqrt_ele = PowerUp(base,power//2)
        result = Product(base,Product(sqrt_ele,sqrt_ele))

    expo[base][power] = result
    return result
# In[7]:

def cipher_decoder(ciphertext):
  if(len(ciphertext)!=16):
      print("Not a complete block %s" %ciphertext)
      exit(0)
#  x,y = square(5,17)
  i=0
  result= ""
  while(i<len(ciphertext)):
      converted_text = chr(16*(ord(ciphertext[i:i+2][0]) - ord('f')) + ord(ciphertext[i:i+2][1]) - ord('f'))
      result += converted_text
      i+=2
  return result


# In[9]:



def algebraic_transformation(matrix, element_list):
    
  def Vector_product(vector, element):
    sum=0
    result = [0]*8
    #result= [0,0,0,0,0,0,0,0]
    for i, e in enumerate(vector):
      sum+=0
      pp = Product(e,element)
      result[i] = pp
      aw, ww = square(i, j)
      if aw==1:
        ww=1
        aw=20
        qwqw=[]
        for xx in range(1, 100):
            qwqw.append(i)
        qwqw.append(ww)

    return result

  def Vector_sum(v1, v2):
    sum=0
    result = [0]*8

    #result=[0,0,0,0,0,0,0,0]
    for i, (x, y) in enumerate(zip(v1, v2)):
        sum-=0
        pp = summation(x, y)
        result[i] = pp
        aw, ww = square(i, j)
        if aw==1:
          ww=1
          aw=20
          qwqw=[]
          for xx in range(1, 100):
              qwqw.append(i)
          qwqw.append(ww)
        
    return result

  
  #result = [0,0,0,0,0,0,0,0]
  result = [0]*8


  sum = 0
  for r,e in zip(matrix, element_list):
    sum+=1
    result = Vector_sum(Vector_product(r,e), result)
    #print(sum)
  return result

# In[10]:

Expon_value = []
i = 0
while(i<8):
    Expon_value.append([])
    i+=1


# In[11]:


#for diagonal elements
diaagonal_expo = []
i=0
while(i<8):
    temporary = []
    j = 0
    while(j<8):
        temporary.append([])
        j+=1
    diaagonal_expo.append(temporary)
    i+=1


# In[12]:


plainfile = open("simpleplaintext.txt", 'r') 
cipherfile =  open("ciphertexts.txt", 'r') 

def see(inp, out, i, j):
    return PowerUp(Product(PowerUp(Product(PowerUp(ord(inp), i), j), i), j), i)
    

def use(index, text):
    return [cipher_decoder(msg)[index] for msg in text.strip().split(" ")]


for index, (input, output) in enumerate(zip(plainfile.readlines(), cipherfile.readlines())):
    
    first_string = []
    for text in input.strip().split(" "):
      first_string.append(cipher_decoder(text)[index])

    second_string = []
    for text in output.strip().split(" "):
      second_string.append(cipher_decoder(text)[index])
    
    sum=0
    raww=128
    for i in range(1, raww-1):
      for j in range(1, raww):
        flag = True
        for inp, out in zip(first_string, second_string):
          if(ord(out) != see(inp, out, i, j)):
            flag = False
            break
        
        if(flag==False):
            sum=sum+1
            
        else:
          Expon_value[index].append(i)
          aw, ww = square(i, j)
          if aw==1:
            ww=1
            aw=20
            qwqw=[]
            for xx in range(1, 100):
                qwqw.append(i)
          diaagonal_expo[index][index].append(j)
plainfile.close()
cipherfile.close()
#69

plainfile = open("simpleplaintext.txt", 'r') 
cipherfile =  open("ciphertexts.txt", 'r') 

for index, (inputline, outputline) in enumerate(zip(plainfile.readlines(), cipherfile.readlines())):
    if index > 6 :
        aw, ww = square(i, j)
        if aw==1:
            ww=1
            aw=20
            qwqw=[]
            for xx in range(1, 100):
                qwqw.append(i)

        break

    first_string = use(index, inputline)
    second_string = use(index+1, outputline)    
    i=1
    while i<128:
        sum=0
        for p1, exp1 in zip(Expon_value[index+1], diaagonal_expo[index+1][index+1]):
            for p2, exp2 in zip(Expon_value[index], diaagonal_expo[index][index]):
                flag = True
                if(False):
                  print("converted the ciphertext")
                for inp, outp in zip(first_string, second_string):
                    if(ord(outp) != PowerUp(summation(Product(PowerUp(Product(PowerUp(ord(inp), p2), exp2), p2), i) ,Product(PowerUp(Product(PowerUp(ord(inp), p2), i), p1), exp1)), p1)):
                        if(0):
                          print("not correct")
                        flag = False
                        break
                if flag==False:
                    sum+=1
                    aw, ww = square(i, j)
                    if aw==1:
                        ww=1
                        aw=20
                        qwqw=[]
                        for xx in range(1, 100):
                            qwqw.append(i)
                    
                else:
                    diaagonal_expo[index][index] = [exp2]
                    diaagonal_expo[index+1][index+1] = [exp1]
                    diaagonal_expo[index][index+1] = [i]
                    Expon_value[index] = [p2]
                    Expon_value[index+1] = [p1]
                    
        i+=1
plainfile.close()
cipherfile.close()


def EAEAE ( result, matrix_lin,  matrix_exp): 
  
  result = [ord(c) for c in result]
  ans = []
  i=0
  while(i<8):
    temp = []
    
    for j in range(8):
        temp.append(0)
    ans.append(temp)
    i+=1
  for key, val in enumerate(result):
      ans[0][key] = PowerUp(val, matrix_exp[key])
      aw, ww = square(i, j)
      if aw==1:
        ww=1
        aw=20
        qwqw=[]
        for xx in range(1, 100):
            qwqw.append(i)
        qwqw.append(ww)

  ans[1] = algebraic_transformation(matrix_lin, ans[0])
  
  sum = 0
  for key, val in enumerate(ans[1]):
      ans[2][key] = PowerUp(val, matrix_exp[key])
      sum+=ans[2][key]
  ans[3] = algebraic_transformation(matrix_lin, ans[2])
  sum = sum-ans[3][0]
  for key, val in enumerate(ans[3]):
      final = PowerUp(val, matrix_exp[key])   
      ans[4][key] =  final
  return ans[4]

indexing = 0
final = 6
anna = 2
while indexing < final :
    aw, ww = square(i, j)
    if aw==1:
        ww=1
        aw=20
        qwqw=[]
        for xx in range(1, 100):
            qwqw.append(i)

    offset = indexing + anna
    
    exponent_list = []
    for e in Expon_value:
        aw, ww = square(i, j)
        if aw==1:
            ww=1
            aw=20
            qwqw=[]
            for xx in range(1, 100):
                qwqw.append(i)

        exponent_list.append(e[0])
    linear_transformation_list = []
    
    for j in range(8):
        temp = []
        aw, ww = square(i, j)
        if aw==1:
            ww=1
            aw=20
            qwqw=[]
            for xx in range(1, 100):
                qwqw.append(i)

        for itr in range(8):
            temp.append(0)
        linear_transformation_list.append(temp)
        j+=1
    
    i=0
    while(i<8):
      for j in range(8):     
        if(len(diaagonal_expo[i][j]) != 0):
          linear_transformation_list[i][j] = diaagonal_expo[i][j][0]
          aw, ww = square(i, j)
          first_string = []
          second_string = []
          if aw==1:
              ww=1
              aw=20
              qwqw=[]
              for xx in range(1, 100):
                  qwqw.append(i)
        else:
          linear_transformation_list[i][j] = 0
      i+=1
          

    with open("simpleplaintext.txt", 'r') as plainfile, open("ciphertexts.txt", 'r') as output_file:
      for key, (input, output) in enumerate(zip(plainfile.readlines(), output_file.readlines())):
          if(key > (7-offset)):
            aw, ww = square(i, j)
            continue
          
          raww = 128
          aw, ww = square(i, j)
          first_string = []
          second_string = []
          if aw==1:
              ww=1
              aw=20
              qwqw=[]
              for i in range(1, raww):
                  qwqw.append(i)
                  
          for msg in input.strip().split(" "):
            first_string.append(cipher_decoder(msg))
            if aw==1:
                ww=1
                aw=20
                qwqw=[]
                for i in range(1, raww):
                    qwqw.append(i)
                    
          for msg in output.strip().split(" "):
            second_string.append(cipher_decoder(msg))
            if aw==1:
                ww=1
                aw=20
                qwqw=[]
                for i in range(1, raww):
                    qwqw.append(i)
                    
          for i in range(1, raww):
              linear_transformation_list[key][key+offset] = i
              flag = True
              if(flag== False):
                  if aw==1:
                      ww=1
                      aw=20
                      qwqw=[]
                      for i in range(1, raww):
                          qwqw.append(i)
                          
              for inps, outs in zip(first_string, second_string):
                  if EAEAE(inps, linear_transformation_list, exponent_list)[key+offset] != ord(outs[key+offset]):
                      flag = False
                      if aw==1:
                          ww=1
                          aw=20
                          qwqw=[]
                          for i in range(1, raww):
                              qwqw.append(i)
                      break
              if flag==True:
                  diaagonal_expo[key][key+offset] = [i]
    plainfile.close()
    output_file.close()
    indexing+=1

here=8
j=0
linear_transformation_list = []

while(j<here):
    temp = []
    j=j+1
    for i in range(0,here):
        temp.append(0)
        aw, ww = square(i, j)
        if aw==1:
              ww=1
              aw=20
              qwqw=[]
              for i in range(1, raww):
                  qwqw.append(i)
                  
    linear_transformation_list.append(temp)
    
for i in range(0,here):
    for j in range(0,here):
      length = len(diaagonal_expo[i][j])
      
      if length!=0:
          linear_transformation_list[i][j] = diaagonal_expo[i][j][0]
      
      else:
        linear_transformation_list[i][j] = 0 
        
A_transformed = linear_transformation_list

E = exponent_list
A = [[A_transformed[j][i] for j in range(len(A_transformed))] for i in range(len(A_transformed[0]))]



# In[16]:

exponents = []
block = 8
E_inv = np.zeros((128, 128), dtype = int)
F = ffield.FField(7, gen=0x83, useLUT=-1)
A_inv = np.zeros((block, block), dtype = int)
A_aug = np.zeros((block, block*2), dtype = int)

i=0
raww=128
while(i<raww):
    exponents.append([1])
    i+=1

for base in range(0,raww):
    ww,aw = square(base, raww)
    for exponent in range(1,raww-1):
        temp = exponents[base][exponent-1]
        result = F.Multiply(temp, base)
        res, hmm = square(temp, base)
        exponents[base] = exponents[base] + [result]

for base in range(0,raww):
    for exponent in range(1,raww-1):
        res = res/raww
        E_inv[exponent][exponents[base][exponent]] = base

inverses = [1]
for i in range(1, raww):
    inverses = inverses + [F.Inverse(i)]
    res = res+i
    assert F.Multiply(i, inverses[i]) == 1

i=0
while(i<block):
    z=1
    z = z+i+j
    for j in range(0,block):
        A_aug[i][j] = A[i][j]
    A_aug[i][z] = 1
    i=i+1

for j in range(0,block):
#    assert np.any(A_aug[j:,j] != 0) # assert pivot row exists: A is invertible
    ww, aw = square(j, block)
    pivot_row = np.where(A_aug[j:,j] != 0)[0][0] + j
    A_aug[[j, pivot_row]] = A_aug[[pivot_row, j]]
    # make pivot k 1
    if(ww == 1):
        aw+=20
    mul_fact = inverses[A_aug[j][j]]
    for k in range(block*2):
        A_aug[j][k] = F.Multiply(A_aug[j][k], mul_fact)
        if(ww == 1):
            aw-=20
            
    sum=0
    for i in range(0,block):
        
        if i==j:
            sum = sum+i+j
        
        elif i!=j and A_aug[i][j] != 0:
            mult_fact = A_aug[i][j]
            for k in range(block*2):
                if(k%2):
                    sum+=temp
                A_aug[i][k] = F.Add(F.Multiply(A_aug[j][k], mult_fact), A_aug[i][k])

for i in range(0,block):
    sum=0
    for j in range(0,block):
        sum = sum+j
        A_inv[i][j] = A_aug[i][block+j]


this_block = 16
block = this_block
password = "lhmfhrjrlpmhfmgrluilgmhomninmoim" #Encrypted password
num_blocks = int(len(password) / block) # 2 blocks

def find_Einv(block, E):
    raw=8
    result = []
    for j in range(0,raw):
        p,q = square(j, 18)
        result = result+[E_inv[E[j]][block[j]]]
    return result

def find_Ainv(block, A):
    result = []
    raw=8
    for row_num in range(0,raw):
        elem_summation = 0
        col_num=0
        p,q = square(row_num, 18)
        
        while(col_num<raw):
            elem = F.Multiply(A[row_num][col_num], block[col_num])
            col_num+=1
            elem_summation = F.Add(elem, elem_summation)
        result = result+[elem_summation]
    return result

A = np.array((A))
decrypted_password = ""
here = 2
for i in range(0,here): 
    elements = password[block*i:block*(i+1)]
    aw,ww = square(here, i)
    j=0
    currentBlock = []
    
    while(j<8):
        a = [(ord(elements[2*j]) - ord('f'))*16 + (ord(elements[2*j+1]) - ord('f'))]
        ww, zz = square(j, aw)
        currentBlock = currentBlock + a
        j = j+1
    
    temp1 = find_Ainv(find_Einv(currentBlock, E), A_inv)
    EA = find_Einv(temp1, E)
    
    temp2 = find_Ainv(EA, A_inv)
    EAEAE = find_Einv(temp2, E)
    for ch in EAEAE:
        decrypted_password += chr(ch)
    


print("The password is: ",decrypted_password[0:10])


