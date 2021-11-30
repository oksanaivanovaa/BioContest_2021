# This implementation based on dynamic pairvise comparison of deltas in sorted arrays

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






def min_delta_for_si(m_sort, a_sort, s_sort_i):  # returns optimal m_sort_i and a_sort_i
    m_sort_answ = m_sort[0]
    a_sort_answ = a_sort[0]
    delta = s_sort_i - (m_sort_answ + a_sort_answ) #if delta<0 then next_delta<delta => answer is first delta
    order = True #'forward' order of s_sort direction, False - reverse
    for i in range(m_sort):
        for j in range(a_sort):
            delta_new = s_sort_i - (m_sort[i]+a_sort[j])
            if delta_new < 0:
                if abs(delta_new) < delta:


            #if m_sort[i]+a_sort[j] < 0:



    return [m_sort_answ, a_sort_answ]


def find_idx_answ(m,a, m_sort, a_sort, s_sort_i):
    answ_m, answ_a = min_delta_for_si(m_sort, a_sort, s_sort_i)
    return [m.index(answ_m) + 1, a.index(answ_a) + 1]


def create_dict_answ_for_s_sort(m, a, m_sort, a_sort, s_sort):
    dicti = dict.fromkeys(s_sort)
    for i in range(len(s_sort)):
        dicti[s_sort[i]] = find_idx_answ(m,a, m_sort, a_sort, s_sort[i])
    return dicti




f = open('problem2_input/3.txt', 'r')
t = int(f.readline())

with open('out.txt', 'a') as o:
    for i in range(t):
        m_n, a_n, s_n, m, a, s = read_test(f)
        m_sort, a_sort, s_sort = sorting(m, a, s)
        dicti = create_dict_answ_for_s_sort(m,a,m_sort, a_sort, s_sort)
        for s_i in s:
            answ = dicti[s_i]  # indexes for j and k
            o.write(' '.join(map(str, answ)) + '\n')




f.close()