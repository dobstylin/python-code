import numpy as np

def numpy_practice():
    """Numpy Practice"""

    a = np.arange(100)
    b = np.arange(0, 100, 10)
    c = np.arange(0, 1, 0.1)
    d = np.random.rand(10,10)
    a.shape = (10,10)
    f = a[4,5]
    g = a[4]
    h = d.sum()
    i = a.max()
    j = b.T
    k = a + d
    l = a * d
    m = np.dot(a, d)
    n = a * d
    return m, n 


def main():
    print(numpy_practice())


if __name__ == '__main__':
    main()
