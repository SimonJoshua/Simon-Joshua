name=('Yusuf and sons')
print('p is the principal,t is the time period, r is the rate of interest and n is the amount')
p=float(input('enter the principal '))
t=float(input('enter the time period '))
r=float(input('enter the rate '))
n=float(input('enter the n '))
si=(p*r*t)/100
ci=p*((1+r)/n)*n*t
print(name)
print('The simple interest is ',si)
print('The compound interest is ',ci)