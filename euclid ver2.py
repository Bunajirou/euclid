print('ax + bx = gcd(a,b)')

a = int(input('a='))
b = int(input('b='))

if( b > a ):
    tmp = a
    a = b
    b = a
#  a,bが互いに素であるとき、ここから必要ない--------------------------------------------------
a_org = a
b_org = b

print('')

r = a  #  次のループを動かすためのとりあえず代入
i = 0  #  式の番号

while( r != 0 ):
    q = a // b
    r = a % b
    
    #print('({0}) {1} = {2} * {3} + {4}'.format(i, a, q, b, r))
    a = b
    b = r
    i += 1
gcd = a    

print('GCD=',gcd,'\n')
#  a,bが互いに素であるとき、ここまで必要ない--------------------------------------------

a = a_org // gcd
b = b_org // gcd
a_org = a
b_org = b

print('{0}x + {1}y = 1\n'.format(a, b))

r = 1
i = 0
qlist = []

while( r != 0 ):
    q = a // b
    r = a % b

    print('({0}) {1} = {2} * {3} + {4}'.format(i, a, q, b, r))
    qlist.append(q)
    a = b
    b = r
    i += 1

print(qlist)

n = i - 2
x1 = qlist[n]
x2 = x1
x3 = 1

for j in range(n, 0, -1):
    x1 = x1 * qlist[j-1] + x3
    tmp = x2
    x2 = x1
    x3 = tmp
    #print(x1,x2,x3)

x3 = -x3

print("x0 = {0}, y0 = {1}\n".format(x3, x1))
print("x = {0} + {1}t, y = {2} - {3}t\n".format(x3, b_org, x1, a_org))