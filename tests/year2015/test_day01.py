import advent_of_code.year2015.day01 as sut


def test():
    assert sut.floor_calculator("(())") == 0
    assert sut.floor_calculator("()()") == 0

    assert sut.floor_calculator("(((") == 3
    assert sut.floor_calculator("(()(()(") == 3
    assert sut.floor_calculator("))(((((") == 3

    assert sut.floor_calculator("())") == -1
    assert sut.floor_calculator("))(") == -1

    assert sut.floor_calculator(")))") == -3
    assert sut.floor_calculator(")())())") == -3
