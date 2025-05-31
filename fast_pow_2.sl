4096
# compute 2^k quickly/efficiently
# specification: input goes in register 2
# output will be placed in register 2 as well
# to be run with fast interpreter
# swap 2 into 3 [1 line]
3/2 1,1/1 2
# place 1 in 5 and 7 [1 line]
35/1 3
# "while" k > 0, add 7 to 5, copy 5 into 7 and 11, then swap 11 into 5, multiplying 5 by 2
1/3 4,1/1 7
5/7 4,1/1 5
77/5 5,1/1 6
5/11 6,1/1 3
2/35 7

