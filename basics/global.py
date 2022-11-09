# a global variable: set to a value outside of any function
g = 'global'

def fn1(n):
    # global declaration not needed because g is not altered
    print(f'n1 = {n}, g = \'{g}\'')

def fn2(n):
    # global declaration needed because g is altered
    global g
    g += ' x'
    print(f'n2 = {n}, g = \'{g}\'')

fn1(1)
fn2(2)
fn1(3)
fn2(4)
fn1(5)