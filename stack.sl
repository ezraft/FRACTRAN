823200
# specification: the stack will be stored in register 2
# the input to be placed in the stack will be in register 3 (first bit)
# push/pop will be determined by register 5 (if 5 is 0, then pop, else push)
# note that only the first bit from 5 must be considered
# 5 must be divided by 2, with the remainder tossed
# the number of cycles will be placed in register 7
# registers 11, 13, 17, 19 will be kept as temporary
# result of pops will be placed in 23

# decrement the number of remaining instructions
# line 1
1/7 2

# pop the first bit from 5, place it in 11
# line 2
11/5 2,1/1 3
# line 3
5/121 3,1/1 4

# if the bit in 11 is 1, then the operation is a push, else pop and place result in 29
# line 4
1/11 8,29/23 4,1/1 5
# line 5
529/29 5,1/1 6
# line 6
29/2 6,1/1 7
# line 7
# return to the start after process ends
2/841 7,23/29 7,1/1 1

# if the operation is a push, then push into the stack
# first pop the first bit from 3 and place it in 13
# line 8
13/3 8,1/1 9
# line 9
3/169 9,1/1 10
# next push that bit into the stack
# line 10
19/2 10,1/1 11
# line 11
4/19 11,2/13 11,1/1 1