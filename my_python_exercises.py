import os
import re
import shutil
from functools import reduce
from pathlib import Path
from string import Template
from typing import Dict, List


template_str: str = \
f'''#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def main():
    r"""
$title 
$level
$question

$test
    """
    pass

#### Your code below

#### Your code above


if __name__ == '__main__':
    main()
'''
tempate: Template = Template(template_str)

questions_file_name: str = 'my-100-python-challenging-programming-exercises/My-100+ Python challenging programming exercises.txt'
questions_file_title_offset: int = 2
dist_dir_name: str = 'my_exercises'

Path(dist_dir_name).mkdir(parents=True, exist_ok=True)
shutil.rmtree(dist_dir_name)
Path(dist_dir_name).mkdir(parents=True, exist_ok=True)

buffer: str = ''
with open(questions_file_name, 'r') as f:
    buffer = f.read()

questions: List[str] = re.split(r'#[-]+#', buffer)
questions = [str(x).strip() for x in questions if len(str(x).strip()) > 0]

for i in range(questions_file_title_offset, len(questions)):
    one: str = questions[i]
    lines: List[str] = [x for x in one.split('\n') if len(str(x).strip()) > 0]

    data: Dict[str, str] = {
        'title': '',
        'level': '',
        'question': '',
        'hints': '',
        'solution': '',
        'test': ''
    }

    key: str = ''
    for line in lines:
        if line.startswith('Question '):
            key = 'title'
        elif line.startswith('Level'):
            key = 'level'
        elif line.startswith('Question:'):
            key = 'question'
        elif line.startswith('Hints'):
            key = 'hints'
        elif line.startswith('Solution'):
            key = 'solution'
        elif line.startswith('Test'):
            key = 'test'

        if key == '':
            continue

        data[key] += f'{line}\n'

    for key in data:
        lines = data[key]
        lines = lines.split('\n')
        lines = map(lambda a: f'    {a}' if not str(a).startswith(' ') else f'{a}', lines)
        lines = reduce(lambda a, b: f'{a}\n{b}', lines)
        data[key] = lines

    source: str = tempate.substitute(data)

    source_file_name: str = f'question_{i-1:02d}.py'
    with open(os.path.join(dist_dir_name, source_file_name), 'w') as f:
        f.write(source)
