from itertools import chain


def multiziperator(*iterable):
    return iter(chain(*zip(*iterable)))
