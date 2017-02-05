import sys

def mergesort(a):
    b = list(a)
    split_merge(b, 0, len(a), a)
    return a

def split_merge(b, begin, end, a):
    if end - begin < 2:
        return a

    middle = (end + begin) / 2

    split_merge(a, begin, middle, b)
    split_merge(a, middle, end, b)

    merge(b, begin, middle, end, a)

def merge(a, begin, middle, end, b):
    i = begin
    j = middle

    for k in xrange(begin, end):
        if i < middle and (j >= end or a[i] <= a[j]):
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
    
def main(args):
    a = [1, 7, 5, 3, 11, 8, 2, 10]
    print(a)
    print(mergesort(a))
    
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
