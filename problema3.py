n=0
suma_p=0
while((n%3!=0)or(n%2==0)):
    n=eval(input("introduceti numarul: "))
    if n%2==0:
        suma_p+=n
print("suma numerelor pare este egala cu ",suma_p)