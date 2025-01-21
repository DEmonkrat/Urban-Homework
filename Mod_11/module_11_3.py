from pprint import pprint
class My_class:
    def __init__(self, a ,b):
        self.a = a
        self.b = b

    def print_ab(self):
        print(self.a, self.b)


def introspection_info(obj):
    intr_res = {}
    intr_res['type'] = type(obj)
    intr_res['atr_meth'] = dir(obj)
    intr_res['callable'] = callable(obj)
    return intr_res


number_info = introspection_info(42)
pprint(number_info)