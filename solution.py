# https://www.hackerrank.com/challenges/designer-door-mat/problem
# Solved using Object Oriented Programming


# a doormat is a type of object
class DoorMat:
    def __init__(self):
        self._design = ""

    def dashes(self, x):
        for i in range(x):
            self._design += "---"

    def embellish(self, x):
        for i in range(x):
            self._design += ".|."

    def welcome(self):
        self._design += "-WELCOME-"

    def newline(self):
        self._design += "\n"

    def print(self):
        print(self._design)


# a designer doormat is a type of doormat with a design spec
class DesignerDoorMat(DoorMat):
    def __init__(self, n):
        DoorMat.__init__(self)
        # top of pattern
        for i in range((n - 1) // 2):
            self.dashes((n - 1) // 2 - i)
            self.embellish(2 * i + 1)
            self.dashes((n - 1) // 2 - i)
            self.newline()
        # middle line
        self.dashes((n - 3) // 2)
        self.welcome()
        self.dashes((n - 3) // 2)
        self.newline()
        # bottom of pattern
        for i in range((n - 1) // 2 - 1, -1, -1):
            self.dashes((n - 1) // 2 - i)
            self.embellish(2 * i + 1)
            self.dashes((n - 1) // 2 - i)
            self.newline()


# driver code
n = int(input().split()[0])
while n % 2 == 0:
    n = int(input("Please supply an odd number: ").split()[0])

D = DesignerDoorMat(n)
D.print()
