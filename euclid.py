import time

print('ax + bx = gcd(a,b)')

a = int(input('a='))
b = int(input('b='))
a2 = a
b2 = b

start = time.time()

print('')

r = a  #  次のループを動かすためのとりあえず代入
i = 0  #  式の番号

while( r != 0 ):
    q = a // b
    r = a % b
    
    #print('(',i,')',a,'=',q,'*',b,'+',r)
    a = b
    b = r
    i += 1
gcd = a    

print('GCD=',gcd)

a = a2 // gcd
b = b2 // gcd

x = 1
r = 0  #  次のループを動かすための0代入

while( r != 1 ):
    x += 1
    r = (a * x) % b
    
y =(1 - a * x ) // b

print('x0 =',x)
print('y0 =',y)
print('x = {0} + {1}t, y = {2} - {3}t'.format(x,b,y,a))

process_time = time.time() - start
print(process_time,'sec')