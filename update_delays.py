import re

file_path = r'c:/xampp/htdocs/Dulces 40/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

def halve_wow(m):
    val = float(m.group(1))
    return f'data-wow-delay="{val / 2:g}s"'

content = re.sub(r'data-wow-delay="([\d\.]+)s"', halve_wow, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated Delays")
