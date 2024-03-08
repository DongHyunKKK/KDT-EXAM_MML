# -----------------------------------------
# 상속(Inheritance)
# - 다중 상속 허용
# - 문법 : class 자식 클래스명(부모클래스명, ...)

class A:
    @ classmethod
    def printInfo(cls):
        print('A')

class B:
    @classmethod
    def printInfo(cls):
        print('B')

class AB(A, B): pass  # A부터 가서 찾는다. A에서 할일 없으면 B에서 찾는다.


class CC(B, A): pass  # B부터 가서 찾는다. B에서 할일 없으면 A에서 찾는다.

ab1 = AB()
ab1.printInfo()

CC.printInfo()