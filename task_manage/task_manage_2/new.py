class Base:
    def __init__(self):
        print("Base initializer")


class A(Base):
    def __init__(self):
        super().__init__()
        print("A initializer")


class B(Base):
    def __init__(self):
        super().__init__()
        print("B initializer")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("C initializer")


c = C()