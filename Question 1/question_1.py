import numpy as np

def path(m, n, mod, div):
    if div ==1:
        s = np.repeat('R', n-1-mod)
        s = np.append(s, 'D')
        s = np.append(s, np.repeat('R', mod))
        s = np.append(s, np.repeat('D', (m-2)))
    else:
        s = np.repeat('D', (div-1))
        s = np.append(s, np.repeat('R', (n-1-mod)))
        s = np.append(s, 'D')
        s = np.append(s, np.repeat('R', (mod)))
        s = np.append(s, np.repeat('D', (m-div-1)))
    return ''.join(s)

def target_fun(m, n, s_num):
    diff = s_num - (1 + m)*m/2
    div = diff // (n-1)
    mod = diff % (n-1)
    return path(m, n, mod, div)

with open('output_question_1','w') as f:
    print("65 {}".format(target_fun(9, 9, 65)), file=f)
    print("72 {}".format(target_fun(9, 9, 72)), file=f)
    print("90 {}".format(target_fun(9, 9, 90)), file=f)
    print("110 {}".format(target_fun(9, 9, 110)), file=f)
    print("87127231192 {}".format(target_fun(90000, 1000000, 87127231192)), file=f)
    print("5994891682 {}".format(target_fun(90000, 1000000, 5994891682)), file=f)