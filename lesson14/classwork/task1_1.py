class PolyndromicString:
    def __call__(self, string):
        print("__call__ calls")
        return string == string[::-1]


def polyndromic_string(string):
    return string == string[::-1]


c = PolyndromicString()
print(type(c))
print(type(polyndromic_string))

print(c("mom"))
print(c("cat"))
print(polyndromic_string("mom"))
print(polyndromic_string("cat"))
