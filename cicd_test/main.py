
def multiply(x: int, y: int) -> int:
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError('Only integer type is accepted')
    return x * y


if __name__ == 'main':
    multiply(5, 6)
