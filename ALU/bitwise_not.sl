76832
# a rework of stack.sl to support bitwise NOT (complement) of a number
# specification: the argument will be stored in register 2
# the number of bits total will be placed in register 7
# registers 3,5,11, 13, 17, 19, 23, 29 will be kept as temporary
# result will be placed in 2

# first clone the number of instructions
# line 1
667/7 1,1/1 2
# line 2
7/29 2,1/1 3
# decrement the number of remaining instructions
# line 3
1/11 3,1/13 3,1/7 4,1/1 11

# pop the first bit from 2, place it in 13
# line 4
13/2 4,1/1 5
# line 5
2/169 5,1/1 6

# if one of 11 and 13 are 1, then push a 1 into 17, else push a zero
# line 6
961/17 6,11/1 7
# line 7
17/31 7,1/143 3,17/1 3

# push result from 17 into 2
# line 8
1/11 8,1/13 8,1/23 9
# line 9
11/17 9,1/1 10
# line 10
17/121 10,1/1 11
# line 11
9/2 11,1/1 12
# line 12
2/3 12,1/1 13
# line 13
2/11 13,1/1 8


