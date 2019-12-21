## <p align="center">`Spyc` - Python object specifications for humans.</p>
---

<p align="center">
Designed after Clojure's great counterpart, `spyc` aims</br>
to combat the rising popularity of static-types checkers</br>
in Python's ecosystem.
</p>

---

# Examples

### **Validations of types**
``` python
from spyc import is_valid

# Works for primitives
assert is_valid(2, int)
assert is_valid("string", str)

# As well as composite-types (classes)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

assert is_valid(Person("Ajo", 22), Person)
```

---
### **Validations via predicates.**
``` python
from spyc import is_valid

def is_even(target):
    return target % 2 == 0

assert is_valid(2, is_even)
assert is_valid(2.0, is_even)
```

---
### **Combining specifications together**
It's possible to combine specifications
via the `either` and `all_of` objects.

`all_of` requires that all specifications be valid.
`either` requires that at least one specification is valid.

``` python
from spyc import is_valid, either, all_of

def is_even(target):
    return target % 2 == 0

even_integer = all_of(int, is_even)
assert is_valid(2, even_integer)
assert not is_valid(1, even_integer)
assert not is_valid(2.0, even_integer)

number = either(int, float)
assert is_valid(2, number)
assert is_valid(2.0, number)
assert not is_valid("string", number)
```
---
### **Validate the members of objects**
Using the `with_members` specification, you can
validate both the existance of members, and apply
specifications on those members themselves.

``` python
from spyc import is_valid, with_members

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# `with_members` can check the existance of members
assert is_valid(Person("name", 21), with_members("name", "age"))
assert not is_valid(object(), with_members("non_existing_member"))

# But it can also check the specifications of those members as well!
assert is_valid(Person("name", 21), with_members(name=str, age=int))

def is_age_valid(target):
    return target > 0

age_spec = all_of(int, is_age_valid)
person_spec = with_members(name=str, age=age_spec)
assert is_valid(Person("name", 21), person_spec)
assert not is_valid(Person("name", -21), person_spec)
```


# Roadmap
Due to the early stage of the project, a lot
of features are currently missing.

Features currently planned:
- **Better validation reporting**: Instead of `True`/`False`, it'll
  be better to report what specifications actually failed in case
  of `either`/`all_of`

- **Collections validations**: Add support for validations on basic
  container types, such as lists, dictionaries, and sets.

- **Conformation of objects according to specifications**: Not unlike the `From` trait from Rust,
  allow to convert objects from one specficiation to another in ease.

- **Automatic specs validation using decorators and type-annotations**


# Contribution
More details soon.