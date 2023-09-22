import advent_of_code.year2015.day01 as sut
import tests.year2015.test_day01_input as input


def test_examples_part1():
    assert sut.floor_calculator_part1("(())") == 0
    assert sut.floor_calculator_part1("()()") == 0

    assert sut.floor_calculator_part1("(((") == 3
    assert sut.floor_calculator_part1("(()(()(") == 3
    assert sut.floor_calculator_part1("))(((((") == 3

    assert sut.floor_calculator_part1("())") == -1
    assert sut.floor_calculator_part1("))(") == -1

    assert sut.floor_calculator_part1(")))") == -3
    assert sut.floor_calculator_part1(")())())") == -3


def test_input_part1():
    assert sut.floor_calculator_part1(input.input) == 232


def test_examples_part2():
    assert sut.floor_calculator_part2(")") == 1

    assert sut.floor_calculator_part2("()())") == 5


def test_input_part2():
    assert sut.floor_calculator_part2(input.input) == 1783
