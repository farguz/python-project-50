from gendiff.formatter import plain as plain
from gendiff.formatter import choose_format as choose_format
from gendiff.formatter import stylish as stylish
from gendiff.formatter import json_format as json_format

from gendiff.generate_diff_tree import generate_diff_tree as generate_diff_tree

__all__ = ('generate_diff_tree',
           'json_format',
           'stylish',
           'choose_format',
           'plain')
