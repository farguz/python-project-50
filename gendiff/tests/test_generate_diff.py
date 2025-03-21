import pytest

from gendiff.generate_diff_tree import (
    check_file_extension,
    get_value,
)


@pytest.mark.parametrize("test_input, expected",
                         [([{'key': 'abc'}, 'key'], 'abc'),
                          ([{}, ''], None),
                          ([{'key': 'abc'}, 'no_key'], None)])
def test_get_value(test_input, expected):
    assert get_value(*test_input) == expected


@pytest.mark.parametrize("test_input, expected",
                         [('test_file.yml', 'yml'),
                          ('', None)])
def test_check_file_extension(test_input, expected):
    assert check_file_extension(test_input) == expected
