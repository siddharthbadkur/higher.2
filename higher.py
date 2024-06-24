my_number=[10,44,23,45,67,90]    
def even_num(n):
    if n%2==0:
        return True
    return False
x=filter(even_num,my_number)
print(x)
print(list(x))

my_number=[10,4,23,45,67,90]   
def odd_num(n):
    if n%2!=0:
        return True
    return False
x=filter(odd_num,my_number)
print(x)
print(list(x))
 
x=lambda a,b,c:2*a+2*b+2*c
print(x(20,30,40))