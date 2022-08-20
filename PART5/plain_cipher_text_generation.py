#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import the necessary files
import pexpect
import numpy as np


# In[5]:


# we will generate plaintexts randomly consisting of char from 'f' to 'u'
mapping = {
 '0000': 'f',
 '0001': 'g',
 '0010': 'h',
 '0011': 'i',
 '0100': 'j',
 '0101': 'k',
 '0110': 'l',
 '0111': 'm',
 '1000': 'n',
 '1001': 'o',
 '1010': 'p',
 '1011': 'u',
 '1100': 't',
 '1101': 's',
 '1110': 'r',
 '1111': 'q'
}


# In[11]:


# generating plaintexts

file = open('simpleplaintext.txt', 'w+')
for i in range(8):
    for j in range (128):
        binary = bin(j)[2:].zfill(8)
        text = 'ff'*i + mapping[binary[:4]] + mapping[binary[4:]] + 'ff'*(8-1-i)
        text +=" " 
        file.write(text)
    file.write("\n")

file.close()


# In[12]:



terminal = pexpect.spawn('/usr/bin/ssh students@172.27.26.188')                     
terminal.expect('students@172.27.26.188\'s password:')
terminal.sendline('cs641a')

terminal.expect('Enter your group name: ', timeout=250) 
terminal.sendline("Enigma")

terminal.expect('Enter password: ', timeout=250)
terminal.sendline("joker777")

terminal.expect('\r\n\r\n\r\nYou have solved 5 levels so far.\r\nLevel you want to start at: ', timeout=250)
terminal.sendline("5")

terminal.expect('.*')
terminal.sendline("go")

terminal.expect('.*')
terminal.sendline("wave")

terminal.expect('.*')
terminal.sendline("dive")

terminal.expect('.*')
terminal.sendline("go")

terminal.expect('.*')
terminal.sendline("read")

terminal.expect('.*')


# In[15]:


plain = open("simpleplaintext.txt", 'r')
cipher = open("ciphertexts.txt",'w')
count=0
here=0

for line in plain.readlines():
    here=here+1
    splitted = line.split()
    for l in splitted:
        count = count+1
        terminal.sendline(l)
        s = str(terminal.before)
        s = s[48:64]
        s = s+" "
        cipher.write(s)
        terminal.expect("Slowly, a new text starts*")
        terminal.sendline("c")
        terminal.expect('The text in the screen vanishes!')
        
        print("progress:",count)
    cipher.write("\n")


