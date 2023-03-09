class Array(list):
    def __init__(self, i=[], t=int, *args, **kwargs):
        super().__init__(i)
        self.t = t

    def append(self, element):
        if not isinstance(element, self.t):
            raise ValueError(f"Element must be {self.t}")
        super().append(element)


l1 = [1, 2, 3]
l1.append("str")


# l1 = list("str")
# print(l1)

a1 = Array(t=int)
# a1.append("str") # ValueError
a1.append(5)
a1.append(2)
a1.append(10)
print(sorted(a1))
