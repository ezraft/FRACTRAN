import sys
INF = 1000000000000000000000000000000
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
prog_val = get_info(prog_input)

while True:
    # state for debug
    print("pc", pc)
    print(prog_val)
    # go = input("-> Step? ")
    # if go != 'y':
    #     break

    ex_inst = False
    for frac in inst[pc]:
        numer = get_info(frac[0])
        denom = get_info(frac[1])

        print("frac formatted")
        mn = INF
        for x in numer.keys():
            print("numer",x, numer[x])
        for x in denom.keys():
            print("denom",x, denom[x])
            if not x in prog_val.keys():
                mn = 0
            else:
                print(denom[x], prog_val[x])
                mn = min(mn, prog_val[x]//denom[x])
        print("mn",mn)
        if denom == 1:
            for x in numer.keys():
                if x in prog_val.keys():
                    prog_val[x] += numer[x]
                else:
                    prog_val[x] = numer[x]
            pc = frac[2] - 1
            ex_inst = True
            break
        elif frac[2] - 1 != pc and mn != 0:
            for x in denom.keys():
                prog_val[x] -= denom[x]
            for x in numer.keys():
                if x in prog_val.keys():
                    prog_val[x] += numer[x]
                else:
                    prog_val[x] = numer[x]
            pc = frac[2] - 1
            ex_inst = True
            break
        elif mn != 0:
            for x in prog_val.keys():
                if x in denom.keys():
                    prog_val[x] -= mn * denom[x]
            for x in numer.keys():
                if x in prog_val.keys():
                    prog_val[x] += mn * numer[x]
                else:
                    prog_val[x] = mn * numer[x]
            pc = frac[2] - 1
            ex_inst = True
            break
    if not ex_inst:
        break

fin = {}
for val in sorted(prog_val.keys()):
    if prog_val[val] != 0:
        fin[val] = prog_val[val]
print(fin)
