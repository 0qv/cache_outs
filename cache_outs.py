
def cache_outs(fn):
    """
    Decorator function; assumes function has no side effects; is deterministic.
    Violations of this include passing in mutables as arguments.
    --
    Caches the results of a function and returns cached results if called with
    the same arguments, trading time for space complexity. Is best used for a
    function that is recursive that reuses values often. Possible to use
    for iterative functions too, if it follows the assumptions, but would likely
    only find use for complex operations that are repeated over and over.
    """
    cache = {}
    def wrapper(*args, **kwargs):
        tempkey = (fn.__name__, id(fn), tuple(args), tuple(kwargs))
        #print(tempkey)
        if tempkey in cache.keys():
            #print("cached value used: " + str(cache[tempkey]) + " : " + str(tempkey))
            return cache[tempkey]
        else:
            tempreturn = fn(*args, **kwargs)
            cache[tempkey] = tempreturn
            #print("new value       :  " + str(cache[tempkey]) + " : " + str(tempkey))
            return tempreturn
    return wrapper
