print("---Pattern Printing---")
'''
*
**
***
****
*****
******
'''
n = 6
for i in range(n+1):
    print(i*"*")
'''
*
***
*****
'''
n = 3
for j in range(n+1):
    print((j*2-1)*"*")