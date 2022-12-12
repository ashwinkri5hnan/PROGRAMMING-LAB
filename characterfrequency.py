def charfr(str):
     dict={}
     for n in str:
          keys=dict.keys()
          if n in  keys:
               dict[n]+=1
          else:
               dict[n]=1
     return dict
string=input("Enter a string")
print(charfr(string))