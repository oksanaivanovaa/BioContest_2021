# Problem2 in final round . Causative Mutation (haploid version)


def read_test(f):
    n, l = map(int, f.readline().strip().split(' '))
    des = []
    g = []
    for i in range(n):
        des.append(f.readline().strip())
        g.append(f.readline().strip())
    return n, l, des, g


def is_pos_k_mut(k, des, g):
    gen_mut = []
    gen_no_mut = []
    for i in range(n):
        mut = des[i]
        gen = g[i][k]
        if mut == '+':
            gen_mut.append(gen)
        else:
            gen_no_mut.append(gen)
    if len(set(gen_mut)) == 1:
        if gen_mut[0] not in gen_no_mut:
            return True
        else:
            return False
    else:
        return False


f = open('input/problem2/02', 'r')
t = int(f.readline())

for i in range(t):
    n, l, des, g = read_test(f)
    with open('out2_02.txt', 'a') as o:
        for k in range(l):
            T = is_pos_k_mut(k, des, g)
            if T:
                o.write(str(k) + ' ' + str(k) + '\n')
                break

f.close()
