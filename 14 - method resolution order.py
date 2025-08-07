class A:
    def __init__(self) -> None:
        print('Class A')
        super().__init__()
    pass

class B(A):
    def __init__(self) -> None:
        print('Class B')
        super().__init__()
    pass

class C(A):
    def __init__(self) -> None:
        print('Class C')
        super().__init__()
    pass

class D(B, C):
    def __init__(self) -> None:
        print('Class D')
        super().__init__()
    pass

print(D.mro())  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
obj = D()