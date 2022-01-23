#  Copyright (c) lzwang 2020-2022, All Rights Reserved.
#  File info: re_tools.py in MoneyMaster (version 0.1)
#  Author: Liangzhuang Wang
#  Email: zhuangwang82@gmail.com
#  Last modified: 2022/1/23 下午12:19

import re
from re import Pattern

# 匹配方括号
MATCH_SQUARE_BRACKETS = re.compile(r'\[(.*?)]')
# 匹配浮点数
MATCH_FLOAT_NUMBER = re.compile(r"[-+]?(?:\d*\.\d+|\d+)")


def match_pattern(pattern: Pattern, string: str):
    result = re.search(pattern, string)
    return result.group() if result else None


def match_square_brackets(text: str):
    return match_pattern(MATCH_SQUARE_BRACKETS, text)


def match_float_number(text: str):
    return match_pattern(MATCH_FLOAT_NUMBER, text)
