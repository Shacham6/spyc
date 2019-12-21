from spec import is_valid, with_members


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def test_checks_the_existance_of_members():
    some_object = object()
    assert not is_valid(some_object, with_members("name"))
    assert is_valid(Person("Ajo", 21), with_members("name", "age"))


def test_checks_both_existance_and_specs_of_checked_members():
    person = Person(name="name", age=21)
    assert is_valid(person, with_members(name=str, age=int))
    assert not is_valid(person, with_members(non_existing_member=str))
    assert not is_valid(person, with_members(name=int))
