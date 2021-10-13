from pathlib import Path
import pickle
import inspect
from hashlib import sha256
from stash import settings


def hash(data):
    return sha256(data.encode()).hexdigest()


def get_file_name(signature):
    body = inspect.getsource(signature.func)
    params = str(signature.args) + str(signature.kwargs)
    func_body = params + body
    return signature.func_name + "_" + hash(func_body)


def get_file_path(signature):
    path = settings.path
    name = get_file_name(signature)
    parent = Path(path)
    parent.mkdir(exist_ok=True)
    return parent / name


def get_stash():
    return Path(settings.path)
