def flatten(iterable, result=None):
    if result == None:
        result = []
    for it in iterable:
        if type(it) in (list, set, tuple):
            flatten(it, result)
        else:
            result.append(it)
    return [i for i in result if i is not None]

