from gendiff.scripts import generate_diff_tree


def test_generate_diff_json():
    path1 = 'gendiff/tests/test_files/file1.json'
    path2 = 'gendiff/tests/test_files/file2.json'
    assert generate_diff_tree(path1, path2) == """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""


def test_generate_diff_yml():
    path1 = 'gendiff/tests/test_files/file1.yml'
    path2 = 'gendiff/tests/test_files/file2.yml'
    assert generate_diff_tree(path1, path2) == """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""


def test_generate_diff_json_nested():
    pass


def test_generate_diff_yml_nested():
    pass