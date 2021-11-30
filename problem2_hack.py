# Problem2 in final round . Causative Mutation (haploid version)
# only 0..9


def read_test(f):
    n, l = map(int, f.readline().strip().split(' '))
    des = []
    g = []
    for i in range(n):
        des.append(f.readline().strip())
        g.append(f.readline().strip())
    return n, l, des, g



f = open('input/problem2/02', 'r')
t = int(f.readline())

for i in range(t):
    n, l, des, g = read_test(f)
    with open('out2_02.txt', 'a') as o:
        o.write(str(0) + ' ' + str(l-1) + '\n')


f.close()
