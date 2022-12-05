sentence=input("enter text to calculate the occurance of each word")
counts=dict()
words=sentence.split()
for word in words:
    if word in counts:
        counts[word]+=1
    else:
        counts[word] = 1
print(counts)