#for calculation
def hello():
    print("this is my first function")
hello()
def calculate():
    x=12
    y=10
    print(x*y)
calculate()

#to give greeting
def majina (fname , lname):
    print(fname +" "+ lname)
majina("Victor", "Philip")
majina("mercy", "joy")
majina("nick","dat")
majina("joy", "jane")
def greatings (name, greating="hello"):
    print(greating +" "+ name )
greatings("Erick")
greatings("joan"+" "+"niaje!")
def welcome (name, welcome="welcome"):
    print(welcome +" "+ name )
welcome("erick")

#to return the maxalue and minvalue
def maxvalue (a,b,c,d,e,f):
    return max(a,b,c,d,e,f)
result=maxvalue(9,1,8,17,45,5)
print(result)
def minvalue (num1,num2,num3,num4,num5):
    return min(num1,num2,num3,num4,num5)
result=minvalue(21,58,47,65,32)
print(result)

#sorting
def sort_list (list):
    return sorted (list)
answer=sort_list([2,4,5,8,9,6,5,3,7])
print(answer)

#priny out numbers
def print_numbers(n):
    for i in range(n):
        print(i)
print_numbers(5)

