#current file
f=open('sentences.txt',mode='r',encoding = 'utf-8')
#new file
n=open('new_text.txt',mode='w',encoding = 'utf-8')
#we split the text into sentences array/list
sentences=f.read().split('\n')
counter=1
for sentence in sentences:
    n.write(str(counter)+'. '+sentence+'\n')
    counter+=1

#4
f=open('sampletext1.txt','r',encoding='utf-8')
txt=f.read().split()
exceptions=['Mr.','Jr.','Ms.','Mrs.','Dr.']
print(txt)
new_text=''
for word in txt:
    if '?' not in word and '!' not in word:
        new_text+=(word + " ")
        #strip checks the front and back of the string for the specified character
        #if the fullstop is in between
        if '.' in word.strip('.') and word not in exceptions:
            pass
        elif '.' in word[-1] and word not in exceptions:
            new_text+="\n"
    else:
        new_text+=(word + "\n")

print(new_text)