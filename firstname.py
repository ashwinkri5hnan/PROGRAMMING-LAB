firstname=[]
length=int(input("how many names do you want to insert"))
print("enter the first name you want to add to list")
for i in range(0,length):
    fname=input("")
    firstname.append(fname)
    count_a =0
for names in firstname:
    count_a+=names.count("a")
print(count_a)