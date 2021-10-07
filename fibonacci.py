def fibb(inl: list = [0, 1], i=0):
    return fibb(inl + [inl[-1] + inl[-2]], i + 1) if i < 997 else inl


print(fibb())
