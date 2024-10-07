# Task 1
def outer_f(inner_fun):
    text = inner_fun('Hi there')
    print(text)

def upper_inner_f(text):
    return text.upper()

outer_f(upper_inner_f)
