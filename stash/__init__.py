from functools import wraps
from pathlib import Path
from collections import namedtuple
import pickle
from stash.utils import get_file_path, get_stash
from stash.types import Signature


def cache(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        signature = Signature(func.__name__, args, kwargs, func)
        if data := load(signature):
            return data
        data = func(*args, **kwargs)
        data = data if data else None
        save(signature, data)

        return data

    return wrapper


def load(signature):
    _file = get_file_path(signature)
    if _file.exists():
        return pickle.load(open(_file, "rb"))
    return None


def save(signature, data):
    _file = get_file_path(signature)
    pickle.dump(data, open(_file, "wb"))


def burn(func):
    """Burns all your function related stash"""
    folder = get_stash()
    func_name = func.__name__
    filter_by = f"{func_name}_*"
    for _file in folder.glob(filter_by):
        _file.unlink()


def loot():
    """Loots all your stash and burns it"""
    folder = get_stash()
    filter_by = "*"
    for _file in folder.glob(filter_by):
        _file.unlink()
