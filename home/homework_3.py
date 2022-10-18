class Add:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return self.val + other.val


class Sub:
    def __init__(self, val):
        self.val = val

    def __sub__(self, other):
        return self.val - other.val


class Mul:
    def __init__(self, val):
        self.val = val

    def __mul__(self, other):
        return self.val * other.val


class Truediv:
    def __init__(self, val):
        self.val = val

    def __truediv__(self, other):
        return round(self.val / other.val, 2)


class Calculator(Add, Mul, Sub, Truediv):
    def __init__(self, val):
        super().__init__(val)


q = Calculator(10)
w = Calculator(2)

print(q + w)
print(q - w)
print(q * w)
print(q / w)
