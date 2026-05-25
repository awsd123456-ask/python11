#coding:utf-8
import os
import re

def extract_and_convert(py_file, output_dir="docs"):
    """提取Python文件信息并转换为Markdown"""
    with open(py_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 提取练习编号和标题
    match = re.search(r'# 习题(\d+):(.+)', content)
    if not match:
        return None
    
    ex_num = match.group(1)
    ex_title = match.group(2).strip()
    
    # 分离代码和笔记
    lines = content.split('\n')
    code_lines = []
    notes = []
    in_notes = False
    
    for line in lines:
        if '# 笔记' in line or '# 注意' in line:
            in_notes = True
            continue
        if in_notes and line.strip().startswith('#'):
            note = line.strip('# ').strip()
            if note:
                notes.append(note)
        elif not in_notes or not line.strip().startswith('#'):
            code_lines.append(line)
    
    code = '\n'.join(code_lines)
    
    # 生成Markdown
    md = f"""# 练习{ex_num}: {ex_title}

## 📝 练习目标

{ex_title}

## 💻 代码示例

```python
{code}
```

## 📚 作者学习笔记

"""
    
    if notes:
        for note in notes:
            md += f"- {note}\n"
    else:
        md += "（作者未添加额外笔记）\n"
    
    md += """
## 🎯 初学者提示

### 运行这个练习
1. 将代码保存为 `.py` 文件
2. 在终端运行代码
3. 观察输出结果

### 练习建议
- 手动输入每一行代码，不要复制粘贴
- 尝试修改代码，观察变化
- 理解每一行的作用
- 遇到问题及时查阅文档
"""
    
    # 写入文件
    output_file = os.path.join(output_dir, f'ex{ex_num}.md')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md)
    
    print(f"✓ 已生成: ex{ex_num}.md - {ex_title}")
    return (ex_num, ex_title)

# 批量转换
content_dir = 'content'
docs_dir = 'docs'

# 获取所有需要转换的文件
files_to_convert = []
for i in range(24, 46):
    py_file = os.path.join(content_dir, f'ex{i}.py')
    if os.path.exists(py_file):
        files_to_convert.append(py_file)

# 特殊文件
for suffix in ['a', 'b', 'c', 'd', 'e']:
    py_file = os.path.join(content_dir, f'ex44{suffix}.py')
    if os.path.exists(py_file):
        files_to_convert.append(py_file)

print(f"找到 {len(files_to_convert)} 个文件需要转换\n")

converted = []
for py_file in files_to_convert:
    result = extract_and_convert(py_file, docs_dir)
    if result:
        converted.append(result)

print(f"\n完成！共转换 {len(converted)} 个文件")
