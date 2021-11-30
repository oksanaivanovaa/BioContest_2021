import numpy as np

def matrix_cre(file):
    A = []
    n, l = map(int, file.readline().split(' '))
    for i in range(n):
        s = file.readline().strip()
        s = [int(digit) for digit in str(s)]
        A.append(s)
    return(A, n, l)

f = open('problem1_input/2.txt', 'r')
t = int(f.readline())

for i in range(t):

    A, n, l = matrix_cre(f)
    A = np.array(A).transpose().tolist()
    A = [str(i) for i in A]

    answ = []
    keys_no = 0
    di = dict()
    for s in A:
        if s not in list(di):
            keys_no += 1
            di[s] = keys_no
        answ.append(di[s])

    with open('out.txt', 'a') as o:
        o.write(str(keys_no)+'\n'+ ' '.join(map(str,answ))+'\n')


f.close()