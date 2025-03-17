from gendiff.formatter import stylish

test_tree_nested = {
    'common': {
        'type': 'nested',
        'children': [{
            'follow': {
                'type': 'added',
                'value': False
            }
        }, {
            'setting1': {
                'type': 'unchanged',
                'value': 'Value 1'
            }
        }, {
            'setting2': {
                'type': 'deleted',
                'value': 200
            }
        }, {
            'setting3': {
                'type': 'changed',
                'old_value': True,
                'new_value': None
            }
        }, {
            'setting4': {
                'type': 'added',
                'value': 'blah blah'
            }
        }, {
            'setting5': {
                'type': 'added',
                'value': {
                    'key5': 'value5'
                }
            }
        }, {
            'setting6': {
                'type': 'nested',
                'children': [{
                    'doge': {
                        'type': 'nested',
                        'children': [{
                            'wow': {
                                'type': 'changed',
                                'old_value': '',
                                'new_value': 'so much'
                            }
                        }]
                    }
                }, {
                    'key': {
                        'type': 'unchanged',
                        'value': 'value'
                    }
                }, {
                    'ops': {
                        'type': 'added',
                        'value': 'vops'
                    }
                }]
            }
        }]
    },
    'group1': {
        'type': 'nested',
        'children': [{
            'baz': {
                'type': 'changed',
                'old_value': 'bas',
                'new_value': 'bars'
            }
        }, {
            'foo': {
                'type': 'unchanged',
                'value': 'bar'
            }
        }, {
            'nest': {
                'type': 'changed',
                'old_value': {
                    'key': 'value'
                },
                'new_value': 'str'
            }
        }]
    },
    'group2': {
        'type': 'deleted',
        'value': {
            'abc': 12345,
            'deep': {
                'id': 45
            }
        }
    },
    'group3': {
        'type': 'added',
        'value': {
            'deep': {
                'id': {
                    'number': 45
                }
            },
            'fee': 100500
        }
    }
}

right_answer_nested = '''{
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

test_tree_not_nested = {'follow': {'type': 'deleted', 'value': False}, 'host': {'type': 'unchanged', 'value': 'hexlet.io'}, 'proxy': {'type': 'deleted', 'value': '123.234.53.22'}, 'timeout': {'type': 'changed', 'old_value': 50, 'new_value': 20}, 'verbose': {'type': 'added', 'value': True}}

right_answer_not_nested = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

def test_generate_formatter_stylish_nested():
    assert stylish(test_tree_nested) == right_answer_nested


def test_generate_formatter_stylish_not_nested():
    assert stylish(test_tree_not_nested) == right_answer_not_nested
