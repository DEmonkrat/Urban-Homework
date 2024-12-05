def apply_all_func (int_list, *functions):
    result = {}
    for func in functions:
        result[func.__name__] = func(int_list)
    return result


int_l = [1,44,3,565,53,23423,565,566]
print(apply_all_func(int_l, min, max, len, sum, sorted))
print()
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))