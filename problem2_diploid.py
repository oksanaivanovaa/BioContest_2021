# Problem2 in final round . Causative Mutation (DIPLOID version)
# Works only for 05 input


def read_test(f):
    n, l = map(int, f.readline().strip().split(' '))
    des = []
    g1 = []
    g2 = []
    for i in range(n):
        des.append(f.readline().strip())
        g1.append(f.readline().strip())
        g2.append(f.readline().strip())
    return n, l, des, g1, g2


def is_pos_k_mut(k, des, g1, g2):
    gen_mut = []
    gen_no_mut = []
    for i in range(n):
        mut = des[i]
        gen1 = g1[i][k]
        gen2 = g2[i][k]
        if mut == '+':
            if gen1 == gen2:
                gen_mut.append(gen1)
            else:
                return False
        else:
            if gen1 == gen2:
                gen_no_mut.append(gen1)
    if len(set(gen_mut)) == 1:
        if gen_mut[0] not in gen_no_mut:
            return True
        else:
            return False
    else:
        return False


f = open('input/problem2/06', 'r')
t = int(f.readline())

for i in range(t):
    n, l, des, g1, g2 = read_test(f)
    with open('out2_06.txt', 'a') as o:
        for k in range(l):
            T = is_pos_k_mut(k, des, g1, g2)
            if T:
                o.write(str(k) + ' ' + str(k) + '\n')
                break

f.close()
