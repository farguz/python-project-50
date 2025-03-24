import pytest

from gendiff.formatter import choose_format
from gendiff.generate_diff_tree import generate_diff_tree


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
    return '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''


@pytest.fixture
def answer_nested_plain():
    return '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''


@pytest.fixture
def answer_nested_json():
    return ('{"common": {"type": "nested", "children": [{"follow": '
            '{"type": "added", "value": false}}, {"setting1": {"type": '
            '"unchanged", "value": "Value 1"}}, {"setting2": {"type": '
            '"deleted", "value": 200}}, {"setting3": {"type": "changed", '
            '"old_value": true, "new_value": null}}, {"setting4": '
            '{"type": "added", "value": "blah blah"}}, {"setting5": '
            '{"type": "added", "value": {"key5": "value5"}}}, '
            '{"setting6": {"type": "nested", "children": [{"doge": '
            '{"type": "nested", "children": [{"wow": {"type": "changed", '
            '"old_value": "", "new_value": "so much"}}]}}, {"key": '
            '{"type": "unchanged", "value": "value"}}, {"ops": {"type": '
            '"added", "value": "vops"}}]}}]}, "group1": {"type": "nested", '
            '"children": [{"baz": {"type": "changed", "old_value": "bas", '
            '"new_value": "bars"}}, {"foo": {"type": "unchanged", "value": '
            '"bar"}}, {"nest": {"type": "changed", "old_value": {"key": '
            '"value"}, "new_value": "str"}}]}, "group2": {"type": '
            '"deleted", "value": {"abc": 12345, "deep": {"id": 45}}}, '
            '"group3": {"type": "added", "value": {"deep": {"id": '
            '{"number": 45}}, "fee": 100500}}}')


@pytest.fixture
def answer_not_nested_stylish():
    return '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


@pytest.fixture
def answer_not_nested_plain():
    return '''Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true'''


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
