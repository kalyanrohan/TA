with open("test.txt",mode='r', encoding = 'utf-8') as f:
    pass
#same thing
#r+ reading and writing
f=open('sentences.txt',mode='r',encoding = 'utf-8')
#x is writing exclusively
g=open('sentences_capitalized.txt',mode='x',encoding = 'utf-8')
sentences=f.read().split('\n')
for sentence in sentences:
    g.write(sentence.upper()+'\n')
print(sentences) 
#reads entire file or specified number of characters
print(f.read(4))
#tells u where the cursor is
print(f.tell())
#reads 1 line at a time
print(f.readline())
#readline reads everything and stores it in an array
lines=f.readlines()
edited_lines=[]
for line in lines:
    edited_lines.append(line.replace('\n',''))
print(lines)
print(edited_lines)
f.close()
# g.close()

#cleaning data
string1='hello there'
print(len(string1))
string1.strip()
print(string1.replace(' ',''))


