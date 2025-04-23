import time

def time_it(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    
    print("\n-------------------------------------------------------------------------------")
    print(f"TIME TAKEN FOR {func.__name__} : {end - start:.4f} seconds")
    print("-------------------------------------------------------------------------------\n")
    return result