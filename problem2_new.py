# This program works well only for 1test in 3.txt in problem2


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




def min_delta_for_si_mi(m_sort_i, a_sort, s_sort_i): # return delta and a_sort_i for each m_sort_i and s_sort_i
    if m_sort_i + a_sort[-1] <= s_sort_i:
        return s_sort_i - (m_sort_i + a_sort[-1]), a_sort[-1]
    elif m_sort_i + a_sort[0] >= s_sort_i:
        return m_sort_i + a_sort[0] - s_sort[-1], a_sort[0]
    delta = abs(s_sort_i - m_sort_i - a_sort[0])
    a_sort_answ = a_sort[0]
    for i in range(1,len(a_sort)):
        summ = m_sort_i + a_sort[i]
        if summ <= 0:
            continue
        else:
            delta_new = abs(s_sort_i - summ)
            if delta_new >= delta:
                continue
            else:
                delta = delta_new
                a_sort_answ = a_sort[i]
                if delta == 0:
                    return [delta, a_sort_answ]
    return [delta, a_sort_answ]


def min_delta_for_si(m_sort, a_sort, s_sort_i):  # returns optimal m_sort_i and a_sort_i
    m_sort_answ = m_sort[0]
    delta, a_sort_answ = min_delta_for_si_mi(m_sort_answ, a_sort, s_sort_i)
    for i in range(1, len(m_sort)):
        delta_new, a_sort_answ_new = min_delta_for_si_mi(m_sort[i], a_sort, s_sort_i)
        if delta_new >= delta:
            continue
        else:
            delta = delta_new
            a_sort_answ = a_sort_answ_new
            m_sort_answ = m_sort[i]
            if delta == 0:
                return [m_sort_answ, a_sort_answ]
    return [m_sort_answ, a_sort_answ]


def find_idx_answ(m,a, m_sort, a_sort, s_sort_i):
    answ_m, answ_a = min_delta_for_si(m_sort, a_sort, s_sort_i)
    return [m.index(answ_m) + 1, a.index(answ_a) + 1]


def create_dict_answ_for_s_sort(m_sort, a_sort, s_sort):
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
        dicti = create_dict_answ_for_s_sort(m_sort, a_sort, s_sort)
        for s_i in s:
            answ = dicti[s_i]  # indexes for j and k
            o.write(' '.join(map(str, answ)) + '\n')




f.close()