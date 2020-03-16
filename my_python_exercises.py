import re
from typing import List, Dict

file_name: str = 'Python-programming-exercises/100+ Python challenging programming exercises.txt'

buffer: str = None
with open(file_name, 'r') as f:
    buffer = f.read()

questions: List = re.split(r'#[-]+#', buffer)
questions = [str(x).strip() for x in questions if len(str(x).strip()) > 0]

for i in range(2, len(questions)):
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

    print(f'title:\t {data["title"]}')
    print(f'level:\t {data["level"]}')
    print(f'question:\t {data["question"]}')
    print(f'hints:\t {data["hints"]}')
    print(f'solution:\t {data["solution"]}')

    print('#'*20)