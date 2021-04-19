import os
import sys
from pathlib import Path


def file_length(filename):
    return os.stat(filename).st_size


def filefunc(dirname, func) -> dict:
    """
    Apply function to the files within the specified directory.
    No recursion is supported.
    """
    path = Path(dirname)
    success_dict = dict()
    failure_dict = dict()
    try:
        if not path.is_dir():
            raise NotADirectoryError
        filenames = [str(pathobj) for pathobj in list(path.glob("*"))]
        for fname in filenames:
            success_dict[fname] = func(fname)
    except Exception:
        failure_dict[dirname] = sys.exc_info()[2]
    return success_dict, failure_dict


if __name__ == "__main__":
    print(filefunc("/Users/pk/ntc", file_length))
