
class MyClass:
    def __init__(self):
        self.public_attribute = "public"

my_object = MyClass()
print(my_object.public_attribute)  # Output: public

class MyClass:
    def __init__(self):
        self._protected_attribute = "protected"

my_object = MyClass()
print(my_object._protected_attribute)  # Output: protected (still accessible)