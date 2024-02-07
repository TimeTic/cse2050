import time
def time_function(funcs, args, n_trials=10):
    """this function is used to to measure the time it takes to run the function and returns the time"""
    result_time =  float("inf")
    for i in range (n_trials):
        start_time = time.time()
        funcs(args)
        end_time = time.time()
        temp_time = end_time- start_time
        if temp_time < result_time:
            result_time = temp_time
        return result_time


def time_function_flexible(f, args, n_trials=10):
    """this function is used to return the min time"""
    result_time =  float("inf")
    for i in range (n_trials):
        start_time = time.time()
        f(*args)
        end_time = time.time()
        temp_time = end_time- start_time
        if temp_time < result_time:
            result_time = temp_time
        return result_time
if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)] # should be 10x slower to operate on every item
    t2 = time_function(test_func, L2)

    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))