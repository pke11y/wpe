

def myrange2(start=0, stop=0, step=1):
    """
    Range function for Python 2.
    """
    result = []
    if not stop:
        stop, start = start, 0
    while start < stop:
        result.append(start)
        start += step
    return result

def myrange3(start=0, stop=0, step=1):
    """
    Range function for Python 3.
    """
    if not stop:
        stop, start = start, 0
    while start < stop:
        yield start
        start += step

if __name__ == "__main__":
    print(myrange2(10))
    print(myrange2(10, 30))
    print(myrange2(10, 30, 3))
    print(myrange3(10))