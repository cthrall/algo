import sys

def quicksort(a, lo, hi):
    if lo < hi:
        p = partition(a, lo, hi)
        quicksort(a, lo, p - 1)
        quicksort(a, p + 1, hi)

    return a
    
def partition(a, lo, hi):
    pivot = a[hi]
    i = lo
    for j in xrange(lo, hi):
        if a[j] <= pivot:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[hi], a[i] = a[i], a[hi]
    return i

def main(args):
    a = [1, 7, 5, 3, 11, 8, 2, 10]
    print(a)
    print(quicksort(a, 0, len(a) - 1))
    
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
