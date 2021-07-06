from stash import cache, Signature
import stash


@cache
def square(number):
    return number ** 2


def test_loot():
    data = 42
    square(data)
    stash.loot()
    assert len(list(stash.utils.get_stash().glob("*"))) == 0


def test_save_and_load_stash():
    stash.loot()
    data = 42
    square_sign = Signature(square.__name__, (data,), {}, square)
    stash.save(square_sign, square(data))
    assert stash.load(square_sign) == data ** 2


@cache
def createUser(name, age, hobbies="being a couch"):
    return {"name": name, "age": age}

def test_load_dict():
    args = ("Vikram", 23)
    kwargs = {"hobbies": "being a couch part 2"}
    user = createUser(*args, **kwargs)
    user_sign = Signature(createUser.__name__, args, kwargs, createUser)
    assert stash.load(user_sign) == user