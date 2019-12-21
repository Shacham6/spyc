from specs import is_valid, with_members


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def test_checks_the_existance_of_members():
    some_object = object()
    assert not is_valid(some_object, with_members("name"))
    assert is_valid(Person("Ajo", 21), with_members("name", "age"))

