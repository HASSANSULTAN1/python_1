
def my_range(start, stop, step):
    result = []
    i = start
    
    if step > 0:
        while i < stop:
            result.append(i)
            i += step
    elif step < 0:
        while i > stop:
            result.append(i)
            i += step
    else:
        raise ValueError("step cannot be zero")
    
    return result

print(my_range(0, 10, 2))