
print(bin(78))

'''
Bitwise Operator AND :
0 1 : 0
0 0 : 0
1 1 : 1
1 0 : 0
'''
print(0 & 1)
print(78 & 55) 

'''
Bitwise Operator OR :
0 1 : 1
0 0 : 1
1 1 : 0
1 0 : 1
'''
print(0 | 1)
print(78 | 55)

#complement
'''
12 = 00001100
1's complement = 11110011 = -13

13 = 00001101
2's complement = 1's complement + 1 = 11110010 + 1 = 11110011 = -13
'''
print(~12)

#XOR
'''
0 0 : 0
0 1 : 1
1 0 : 1
1 1 : 0
'''
print(44 ^ 22)

#Leftshift
'''
44 = 00101100
44 << 2 = 10110000
'''
print(44 << 2)

#Rightshift
'''
44 = 00101100
44 >> 2 = 00001011
'''
print(44 >> 2)