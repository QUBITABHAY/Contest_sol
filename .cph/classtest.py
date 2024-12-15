# class NSTStudets:
#     school = "Newton"
#     def __init__(self, val, val1):
#         self.name = val
#         self.sur = val1
#         self.full = val + " " + val1
#     def rev_print(self):
#         print(self.sur + " " + self.name)

# s1 = NSTStudets("Abhay", "Pratap")
# s2 = NSTStudets("Mishi", "Shukla")
# t = type(s2)
# n = t.__name__
# # print(n)
# print(s2.name)
# print(s2.sur)
# print(s2.full)

# s1.rev_print()
# s2.rev_print()
# print(NSTStudets.school)s
# print(NSTStudets.__name__)
# class hh:
#     num1 = 2


class fractional:
    def __init__(self, numerator, denominator):
        self.nume = numerator
        self.den = denominator
    def print(self):
        print(str(self.nume) + "/" + str(self.den))
    def add(self, other):
        n1 = self.nume
        d1 = self.den
        n2 = other.nume
        d2 = other.den
        return fractional(((n1 * d2) + (n2 * d1) + "/" + (d1 * d2)))
f1 = fractional(2, 3)
f2 = fractional(3, 5)
f3 = f1.add(f2)
# f1.print()
# f2.print()
f3.print()