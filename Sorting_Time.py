from Sorting import *

def time_function(function, *args, **kwargs):
    import datetime
    start = datetime.datetime.now()
    function(*args, **kwargs)
    end = datetime.datetime.now()
    return end - start

def main():
    from random import shuffle

    N = 5000
    for func, name in [(mergesort,"Mergesort"), (bubble_sort, "Bubble Sort"), (selection_sort,"Selection Sort")]:
        A = list(range(N))
        shuffle(A)
        print(name, ": ", time_function(func,A))

if __name__ == "__main__":
    main()
