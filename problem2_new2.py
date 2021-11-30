# This program based on matrixes
# Good, but one test (string out of ~200000) failed!! in 3.txt

import numpy as np

def read_test(f):
    m_n, a_n, s_n = map(int, f.readline().split(' '))
    m = list(map(lambda x: int(1000000*x), list(map(float, f.readline().strip().split(' ')))))
    a = list(map(lambda x: int(1000000*x), list(map(float, f.readline().strip().split(' ')))))
    s = list(map(lambda x: int(1000000*x), list(map(float, f.readline().strip().split(' ')))))
    return m_n, a_n, s_n, m, a, s


def sorting(m, a, s):
    m_sort = sorted(set(m))
    a_sort = sorted(set(a))
    s_sort = sorted(set(s))
    return m_sort, a_sort, s_sort






def min_delta_for_si(m_sort, a_sort, s_sort_i, M):  # returns optimal m_sort_i and a_sort_i
    M_delta = abs(M - s_sort_i)
    min_idx = M_delta.argmin()
    k_n = M_delta.shape[1]
    j = min_idx // k_n
    k = min_idx - j*k_n
    m_sort_answ = m_sort[j]
    a_sort_answ = a_sort[k]
    return [m_sort_answ, a_sort_answ]


def find_idx_answ(m,a, m_sort, a_sort, s_sort_i, M):
    answ_m, answ_a = min_delta_for_si(m_sort, a_sort, s_sort_i, M)
    return [m.index(answ_m) + 1, a.index(answ_a) + 1]


def create_dict_answ_for_s_sort(m, a, m_sort, a_sort, s_sort, M):
    dicti = dict.fromkeys(s_sort)
    for i in range(len(s_sort)):
        dicti[s_sort[i]] = find_idx_answ(m,a, m_sort, a_sort, s_sort[i], M)
    return dicti




f = open('problem2_input/3.txt', 'r')
t = int(f.readline())

with open('out.txt', 'a') as o:
    for i in range(t):
        m_n, a_n, s_n, m, a, s = read_test(f)
        m_sort, a_sort, s_sort = sorting(m, a, s)
        M = np.add.outer(m_sort, a_sort)
        M[M <= 0] = 2000000000 #abs(M.max())+1
        dicti = create_dict_answ_for_s_sort(m,a,m_sort, a_sort, s_sort, M)
        for s_i in s:
            answ = dicti[s_i]  # indexes for j and k
            o.write(' '.join(map(str, answ)) + '\n')




f.close()