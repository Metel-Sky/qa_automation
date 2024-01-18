class Simple:
    def __init__(self, value):
        self.value = value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value


obj1 = Simple(5)
obj2 = Simple(10)

print("Not Equal:", obj1 != obj2)
print("Less Than:", obj1 < obj2)
print("Less Than or Equal:", obj1 <= obj2)
print("Greater Than:", obj1 > obj2)
print("Greater Than or Equal:", obj1 >= obj2)
