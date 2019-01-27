from sample import Grid

def test_init_01():
    x = Grid()
    assert x.is_valid() is False
    y = Grid([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert y.is_valid() is True

def dest_init_02():
    x = Grid()
    y = Grid([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert str(x) == '0, 0, 0, 0, 0, 0, 0, 0, 0'
    assert str(y) == '1, 2, 3, 4, 5, 6, 7, 8, 9'


# end of file
