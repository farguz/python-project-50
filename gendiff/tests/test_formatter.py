import pytest

from gendiff.engine import choose_format, generate_diff_tree


def open_file(link):
    with open(link, 'r') as file:
        return file.read()
    

@pytest.fixture
def paths_json_nested():
    return ('gendiff/tests/test_files/file3.json',
            'gendiff/tests/test_files/file4.json')


@pytest.fixture
def paths_json_not_nested():
    return ('gendiff/tests/test_files/file1.json',
            'gendiff/tests/test_files/file2.json')


@pytest.fixture
def paths_yml_nested():
    return ('gendiff/tests/test_files/file3.yml',
            'gendiff/tests/test_files/file4.yml')


@pytest.fixture
def paths_yml_not_nested():
    return ('gendiff/tests/test_files/file1.yml',
            'gendiff/tests/test_files/file2.yml')


@pytest.fixture
def answer_nested_stylish():
    return open_file('gendiff/tests/test_files/answer_nested_stylish.txt')


@pytest.fixture
def answer_nested_plain():
    return open_file('gendiff/tests/test_files/answer_nested_plain.txt')


@pytest.fixture
def answer_nested_json():
    return open_file('gendiff/tests/test_files/answer_nested_json.txt')


@pytest.fixture
def answer_not_nested_stylish():
    return open_file('gendiff/tests/test_files/answer_not_nested_stylish.txt')


@pytest.fixture
def answer_not_nested_plain():
    return open_file('gendiff/tests/test_files/answer_not_nested_plain.txt')


@pytest.fixture
def test_tree_empty():
    return {}


@pytest.fixture
def answer_empty():
    return ''


def test_generate_tree_and_choose_format(
        paths_json_not_nested,
        paths_json_nested,
        paths_yml_not_nested,
        paths_yml_nested,
        answer_not_nested_stylish,
        answer_nested_stylish,
        answer_not_nested_plain,
        answer_nested_plain,
        answer_nested_json,
        test_tree_empty,
        answer_empty):
    
    assert choose_format(test_tree_empty) == answer_empty
    
    assert choose_format(
        generate_diff_tree(*paths_json_not_nested), 
        'stylish') == answer_not_nested_stylish
    
    assert choose_format(
        generate_diff_tree(*paths_json_nested)) == answer_nested_stylish
    
    assert choose_format(
        generate_diff_tree(*paths_yml_not_nested), 
        'plain') == answer_not_nested_plain
    
    assert choose_format(
        generate_diff_tree(*paths_yml_nested), 
        'plain') == answer_nested_plain
    
    assert choose_format(
        generate_diff_tree(*paths_yml_nested), 
        'json') == answer_nested_json
