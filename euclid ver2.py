print('ax + bx = gcd(a,b)')

a = int(input('a='))
b = int(input('b='))
a_o = a  #  ax + bx = gcd(1a,b)を出力するためにおいてあるけど
b_o = b  #  正直なところ邪魔でしかない
swap_flag = 0

if( b > a ):
    tmp = a
    a = b
    b = tmp
    swap_flag = 1
#  a,bが互いに素であるとき、ここから必要ない↓↓↓--------------------------------------------------
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

#print('GCD=',gcd,'\n')
#  a,bが互いに素であるとき、ここまで必要ない↑↑↑--------------------------------------------
print('{0}x + {1}y = {2}'.format(a_o, b_o, gcd))  #  これどうしよう

a = a_org // gcd
b = b_org // gcd
a_org = a
b_org = b

r = 1
i = 0
qlist = []

while( r != 0 ):
    q = a // b
    r = a % b

    #print('({0}) {1} = {2} * {3} + {4}'.format(i, a, q, b, r))
    qlist.append(q)
    a = b
    b = r
    i += 1

n = i - 2
y = qlist[n]
x2 = y
x = 1

for j in range(n, 0, -1):
    y = y * qlist[j-1] + x
    tmp = x2
    x2 = y
    x = tmp

if( i % 2 == 1):  #  式の数が奇数ならx,偶数ならyをマイナスにする
    x = -x
else:
    y = -y

print("")
if( swap_flag == 0):  #  a,bを入れ替えたかどうかの場合分け
    print('x0 = {0}, y0 = {1}'.format(x, y))
    print('x = {0} + {1}t, y = {2} - {3}t\n'.format(x, b_org, y, a_org))
else:
    print('x0 = {0}, y0 = {1}'.format(y, x))
    print('x = {0} - {1}t, y = {2} + {3}t\n'.format(y, a_org, x, b_org))