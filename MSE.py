#import library
import numpy as np
import matplotlib.pyplot as plt
import math

#load input
x=[]
y=[]
check=True
with open ('input.txt','r') as f:
  for line in f:
    #print(line)
    try:
      (_x,_y)=line.split(' ')
      x.append(float(_x))
      y.append(float(_y))
      count = x.count
    except ValueError:
      check=False
      print("Oops!Check Input,plz...")
print(x)
print(y)
#check input
if check:
  if len(x)==len(y):
    print("Input Satisfied")
  else:
    print("Check Input")

plt.scatter(x,y)


#define function
def u0(x):
  return 1
def u1(x):
  return x
def u2(x):
  return x**2
def u3(x):
  return x**3
def u4(x):
  return x**4
def u5(x):
  return math.sin(x)
def u6(x):
  return math.cos(x)
def u7(x):
  return math.sin(2*x)
def u8(x):
  return math.cos(2*x)

#tra ve ma tran sau khi thay cac x vao function u  
def pack1(u,x):
    result=[]
    for i in range(len(u)):
        temp=list(map(u[i],x))
        result.append(temp)
    return np.array(result).T


def pack2(theta):
    return theta.T@theta

def pack3(theta,M,y):
    print(y@theta)
    return np.linalg.inv(M)@((y@theta).T)

u=[u0,u1,u2,u3]

theta=pack1(u,x)
print(theta)

M=pack2(theta)
print(M)

a=pack3(theta,M,y)
print('Ma tran he so la: ')
print(a)

def find_y(x,u,a):
  y=0
  for i in range (0,len(u)):
    y=y+a[i]*u[i](x)
  return y

def graph(x,y,u,a):
  x_test=np.linspace(min(x),max(x),100000)
  y_test=[]
  for i in range (0,len(x_test)):
    y_test.append(find_y(x_test[i],u,a))
  plt.scatter(x, y, s=30)
  plt.plot(x_test, y_test, 'r')


graph(x,y,u,a)
plt.show()



