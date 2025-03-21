p=int(input("place enter principale"))
r=int(input("enter rate"))
t=int(input("enter time"))
amount=p*(1+r/100)**t
ci=amount-p
print(round(ci,2))
    
    
