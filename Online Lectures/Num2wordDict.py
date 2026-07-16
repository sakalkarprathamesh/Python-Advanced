#create Dict of zero to nine

dict= {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}

#accept input from user

nos= input("Enter number:")

#checking nos datatype

print(type(dict))

#split the sting into chunks

for x in nos:
    print(dict[int(x)], end=" ")