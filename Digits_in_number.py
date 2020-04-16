# Code_snippets

///A. Find out number of digits in a number using python
    Method 1 
///
no=float(input("enter the number"))
digits=0 
while(n!=0): 
    n=n//10
    digits+=1 
print("number of digits are",digits) 



//Method 2: 

no=int(input())
print(Len(str(no)))  //convert int to string
