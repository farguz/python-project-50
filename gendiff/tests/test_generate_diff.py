from gendiff.scripts import generate_diff_json


def test_generate_diff_json():
    path1 = 'gendiff/tests/test_files/file1.json'
    path2 = 'gendiff/tests/test_files/file2.json'
    assert generate_diff_json(path1, path2) == """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""