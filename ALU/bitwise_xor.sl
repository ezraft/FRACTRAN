979960197888
# a rework of stack.sl to support bitwise XOR of two numbers
# specification: the first argument will be stored in register 2
# the second argument will be in register 3
# the number of bits total will be placed in register 7
# registers 5,11, 13, 17, 19, 23, 29 will be kept as temporary
# result will be placed in 2

# first clone the number of instructions
# line 1
667/7 1,1/1 2
# line 2
7/29 2,1/1 3
# decrement the number of remaining instructions
# line 3
1/11 3,1/13 3,1/7 4,1/1 11

# pop the first bit from 3, place it in 11
# line 4
11/3 4,1/1 5
# line 5
3/121 5,1/1 6

# pop the first bit from 2, place it in 13
# line 6
13/2 6,1/1 7
# line 7
2/169 7,1/1 8

# if one of 11 and 13 are 1, then push a 1 into 17, else push a zero
# line 8
961/17 8,1/1 9
# line 9
17/31 9,1/143 3,1/13 10,1/11 10,1/1 3
# line 10
# return to start
17/1 3

# push result from 17 into 2
# line 11
1/11 11,1/13 11,1/23 12
# line 12
11/17 12,1/1 13
# line 13
17/121 13,1/1 14
# line 14
9/2 14,1/1 15
# line 15
2/3 15,1/1 16
# line 16
2/11 16,1/1 11


