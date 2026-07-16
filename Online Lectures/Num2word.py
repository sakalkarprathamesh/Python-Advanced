#convert the given number to words


#create list of zero to nine

ls = ("zero","one","two","three","four","five","six","seven","eight","nine")

#accept input from user

nos= input("enter number:")

#checking nos datatype

print(type(nos))

#split the sting into chunks

for x in nos:
    print(ls[int(x)], end=" ")