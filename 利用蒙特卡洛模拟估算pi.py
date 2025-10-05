import numpy as np
def get_pi(num):
    n = num
    points = np.random.rand(2, n)
    m = np.sum(np.where(((points[0]**2 + points[1]**2)**0.5) < 1, 1, 0))
    return 4 * m / n
lst=[]
dart = input()
while dart:
    dart=int(dart)
    lst.append(dart)
    dart = input()
for dart in lst:
    if dart == 0:
        exit()
    else:
        pi = get_pi(dart)
        print(('%.9f' % pi))