from numba.pycc import CC

cc = CC('my_module')
cc.verbose = True

@cc.export('my_add', 'f8 (f8, f8)')
def my_add(x, y):
    return x+y

cc.compile()

