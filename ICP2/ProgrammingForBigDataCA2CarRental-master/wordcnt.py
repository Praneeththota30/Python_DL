f= open("names.txt","r+")
output= open("output.txt","w")
i = []
wordcount = {}
for i in f.read().split():
    if i not in wordcount:
             wordcount[i] = 1
    else:
             wordcount[i] += 1

print(wordcount)
output.write(str(wordcount))
f.close()
