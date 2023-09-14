class A:
    def spam(self):
        print(1)

    def tester(self):
        print('This is just a test method.')

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()
B().tester()