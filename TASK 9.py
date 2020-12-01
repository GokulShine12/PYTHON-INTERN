#lambda fn that multiply argument x with argument y
g=lambda x,y:x*y
print(g(8,5))

#fibonacci series to n
def fib(n):
    s=[0,1]
    any(map(lambda _:s.append(s[-1]+s[-2]),range(2,n)))
    print(s)
n=int(input("Number : "))
fib(n)

#multiply each number of list with a no
l=list(range(30))
l=list(map(lambda n:n*10,l))
print(l)

#nos divisible by 9
l=list(range(50))
l1=list(filter(lambda n:(n%9==0),l))
print(l1)

#count the even nos in the list
l=list(range(1,30))
count=len(list(filter(lambda n:(n%2==0) ,l)))
print(count)
