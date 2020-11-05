n=1
nr=0
suma_p=0
suma_n=0
nr_p=0
nr_n=0
while n<=12:
    nr=eval(input("introdu   temperatura:"))
    if nr>=0:
        suma_p+=nr
        nr_p+=1
    else:
        suma_n+=nr
        nr_n+=1
        n+=1
print("media anuala a temperaturii pozitive este egala cu ",suma_p/nr_p)
print("media anuala a temperaturilor negative este egala cu ",suma_n/nr_n)