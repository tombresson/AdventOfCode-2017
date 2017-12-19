import re

class Register(object):
    def __init__(self, name, value):
        self.name: str = name
        self.value: int = value


def inc(reg: Register, val: int):
    reg.value += val


def dec(reg: Register, val: int):
    reg.value -= val


def eq(left: object, right: object):
    left.__eq__(right)


def ne(left: object, right: object):
    left.__ne__(right)


def gt(left: object, right: object):
    left.__gt__(right)


def ge(left: object, right: object):
    left.__ge__(right)


def lt(left: object, right: object):
    left.__lt__(right)


def le(left: object, right: object):
    return left.__le__(right)

def main():

    reg_fcn = {'inc': inc, 'dec': dec}
    cmp_fcn = {'==': eq, '!=': ne, '>': gt, '>=': ge, '<': lt, '<=': le}

    data_file = open("Data/Day8_data.txt", "r")

    # Process all lines in file
    for line in data_file:
        tokens = re.findall(r'(\S+)', line)

        #4, 5 and 6 are the conditional




if __name__ == "__main__":
    main()