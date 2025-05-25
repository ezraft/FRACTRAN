import sys

# utilities
small_prime_list = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
sys.set_int_max_str_digits(10000000)
# take number and return array of primes and multiplicities in factorization
def get_info(num):
    prime_factors = {}
    num_copy = num
    for prime in small_prime_list:
        while num_copy % prime == 0:
            num_copy //= prime
            if prime not in prime_factors.keys():
                prime_factors[prime] = 1
            else:
                prime_factors[prime] += 1
    return prime_factors

# input file
if len(sys.argv) < 2:
    print("Error: Provide input file.")
    exit(1)

#read program
with open(sys.argv[1], 'r') as f:
    asm = f.read().strip()

#parse program
unfiltered_lines = asm.split("\n")
removed_comments = []
for x in unfiltered_lines:
    if len(x) == 0 or x[0] == '#':
        continue
    removed_comments.append(x)
unfiltered_lines = removed_comments
prog_input = int(unfiltered_lines[0])
instruction_lines = unfiltered_lines[1:]
inst = [[[int(x) for x in ins.split(" ")[0].split('/')] +[int(ins.split(" ")[1])] for ins in line.split(",")] for line in instruction_lines]

# for debugging
# print(prog_input)
# print(inst)

#run program
pc = 0
prog_val = prog_input

while True:
    # state for debug
    print("pc", pc)
    print(prog_val)
    print(get_info(prog_val))
    # go = input("-> Step? ")
    # if go != 'y':
    #     break

    ex_inst = False
    for frac in inst[pc]:
        if prog_val % frac[1] == 0:
            prog_val = prog_val // frac[1]
            prog_val = prog_val * frac[0]
            pc = frac[2] - 1
            ex_inst = True
            break
    if not ex_inst:
        break

print(prog_val)
print(get_info(prog_val))
