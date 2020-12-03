# program using zip() function and list() function, create a merged list of tuples from the two lists given
list1=[1,2,3,4,5,6]
list2=[10,20,30,40,50,60]
a=zip(list1,list2)
print(tuple(a))

# create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples.
number=range(1,8)
list3=[5,10,15,20,25,30,35,40]
b=zip(number,list3)
print(tuple(b))

# Using sorted() function, sort the list in ascending order.
list4=[5,40,77,98,12,76,45,57,33,60]
sort=sorted(list4)
print(sort)

# program using filter function, filter the even numbers so that only odd numbers are passed to the new list.
list5=[41,42,43,44,45,46,47,48,49,50]
newlist=list(filter(lambda x:(x%2!=0),list5))
print(newlist)

