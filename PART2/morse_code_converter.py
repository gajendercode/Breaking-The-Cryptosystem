vocab = {'A':'.-', 'B':'-...',\
                    'C':'-.-.', 'D':'-..', 'E':'.',\
                    'F':'..-.', 'G':'--.', 'H':'....',\
                    'I':'..', 'J':'.---', 'K':'-.-',\
                    'L':'.-..', 'M':'--', 'N':'-.',\
                    'O':'---', 'P':'.--.', 'Q':'--.-',\
                    'R':'.-.', 'S':'...', 'T':'-',\
                    'U':'..-', 'V':'...-', 'W':'.--',\
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',\
                    '1':'.----', '2':'..---', '3':'...--',\
                    '4':'....-', '5':'.....', '6':'-....',\
                    '7':'--...', '8':'---..', '9':'----.',\
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',\
                    '?':'..--..', '/':'-..-.', '-':'-....-',\
                    '(':'-.--.', ')':'-.--.-'}
new_vocab = {v:k for k,v in vocab.items()}
mc = '-.-. .-. -.-- .--. - .- -. .- .-.. -.-- ... .. ...'
mc = mc.split(' ')
out = ''
for i in mc:
    out +=new_vocab[i]
print(out)# your code goes here
