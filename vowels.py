word=input("enter a word")
vowels=["a","e","i","o","u"]
vowelist=[]
for i in word:
    if i in vowels:
        vowelist.append(i)
print(vowelist)