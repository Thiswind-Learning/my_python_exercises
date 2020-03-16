import os
import re
import shutil
from functools import reduce
from pathlib import Path
from string import Template
from typing import Dict, List


width_chars = 64
template_str: str = \
    f'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
{'#' * width_chars}
#
$title
$level
#
{'#' * width_chars}
#
$question
#
$hints
#
{'#' * width_chars}
'''
tempate: Template = Template(template_str)

questions_file_name: str = 'Python-programming-exercises/100+ Python challenging programming exercises.txt'
questions_file_title_offset: int = 2
dist_dir_name: str = 'my_exercises'

Path(dist_dir_name).mkdir(parents=True, exist_ok=True)
shutil.rmtree(dist_dir_name)
Path(dist_dir_name).mkdir(parents=True, exist_ok=True)

buffer: str = None
with open(questions_file_name, 'r') as f:
    buffer = f.read()

questions: List = re.split(r'#[-]+#', buffer)
questions = [str(x).strip() for x in questions if len(str(x).strip()) > 0]

for i in range(questions_file_title_offset, len(questions)):
    one: str = questions[i]
    lines: List[str] = [x for x in one.split('\n') if len(str(x).strip()) > 0]

    data: Dict = {
        'title': '',
        'level': '',
        'question': '',
        'hints': '',
        'solution': ''
    }

    key = ''
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

        if key == '':
            continue

        data[key] += f'{line}\n'

    source: str = tempate.substitute(data)
    lines: List = source.split('\n')
    lines = [x for x in lines if len(x) > 0]
    lines = map(lambda a: a if str(a).startswith('#') else '# ' + a, lines)
    source = reduce(lambda a, b: a + '\n' + b, lines)

    source_file_name: str = f'question_{i-1}.py'
    with open(os.path.join(dist_dir_name, source_file_name), 'w') as f:
        f.write(source)
