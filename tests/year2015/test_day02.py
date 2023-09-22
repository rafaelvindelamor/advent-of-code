import advent_of_code.year2015.day02 as sut
import tests.year2015.test_day02_input as input


def test_examples_part1():
    assert sut.wrapping_calculator_part1(["2x3x4"]) == 58

    assert sut.wrapping_calculator_part1(["1x1x10"]) == 43


def test_input_part1():
    assert sut.wrapping_calculator_part1(input.input.splitlines()) == 1588178


def test_examples_part2():
    assert sut.ribbon_calculator_part2(["2x3x4"]) == 34

    assert sut.ribbon_calculator_part2(["1x1x10"]) == 14


def test_input_part2():
    assert sut.ribbon_calculator_part2(input.input.splitlines()) == 3783758
