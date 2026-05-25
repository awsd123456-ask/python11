#coding:utf-8
import os
import re

def extract_exercise_info(filepath):
    """从Python文件中提取练习信息"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 提取标题
    title_match = re.search(r'# 习题(\d+):(.+)', content)
    if title_match:
        ex_num = title_match.group(1)
        ex_title = title_match.group(2).strip()
    else:
        ex_num = os.path.basename(filepath).replace('ex', '').replace('.py', '')
        ex_title = "练习"

    return ex_num, ex_title, content

def convert_to_markdown(py_file, output_dir):
    """将Python练习文件转换为Markdown"""
    ex_num, ex_title, content = extract_exercise_info(py_file)

    # 分离代码和注释
    lines = content.split('\n')
    code_lines = []
    notes = []
    in_notes_section = False

    for line in lines:
        if line.strip().startswith('# 笔记') or line.strip().startswith('# 注意'):
            in_notes_section = True
            continue

        if in_notes_section and line.strip().startswith('#'):
            notes.append(line.strip('# ').strip())
        elif not in_notes_section or not line.strip().startswith('#'):
            code_lines.append(line)

    # 生成Markdown内容
    md_content = f"""# 练习{ex_num}: {ex_title}

## 📝 练习目标

{ex_title}

## 💻 代码示例

```python
{''.join(code_lines)}
```

## 📚 作者学习笔记

"""

    if notes:
        for note in notes:
            if note:
                md_content += f"- {note}\n"
    else:
        md_content += "（作者未添加额外笔记）\n"

    md_content += """
## 🎯 初学者提示

### 运行这个练习
1. 将代码保存为 `.py` 文件
2. 在终端运行：`python ex{}.py`
3. 观察输出结果

### 常见问题
- 如果遇到中文显示问题，确保文件开头有 `#coding:utf-8`
- Python 2 和 Python 3 的 print 语法不同，这些代码是 Python 2 版本

### 练习建议
- 不要只是复制代码，要自己手动输入每一行
- 尝试修改代码中的值，看看会发生什么
- 理解每一行代码的作用后再继续下一个练习

""".format(ex_num)

    # 写入文件
    output_file = os.path.join(output_dir, f'ex{ex_num}.md')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md_content)

    print(f"✓ 已生成: ex{ex_num}.md - {ex_title}")
    return ex_num, ex_title

def main():
    content_dir = 'content'
    docs_dir = 'docs'

    # 确保docs目录存在
    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)

    # 获取所有练习文件
    exercise_files = []
    for filename in os.listdir(content_dir):
        if filename.startswith('ex') and filename.endswith('.py'):
            match = re.match(r'ex(\d+)\.py', filename)
            if match:
                exercise_files.append((int(match.group(1)), filename))

    exercise_files.sort()

    print(f"找到 {len(exercise_files)} 个练习文件")
    print("开始转换...\n")

    # 转换所有文件
    converted = []
    for num, filename in exercise_files:
        filepath = os.path.join(content_dir, filename)
        try:
            ex_num, ex_title = convert_to_markdown(filepath, docs_dir)
            converted.append((ex_num, ex_title))
        except Exception as e:
            print(f"✗ 转换失败: {filename} - {e}")

    print(f"\n完成！共转换 {len(converted)} 个文件")

    # 生成SUMMARY.md
    generate_summary(converted, docs_dir)

def generate_summary(exercises, docs_dir):
    """生成GitBook的SUMMARY.md目录"""
    summary_content = """# Summary

* [介绍](README.md)

"""

    # 按章节分组
    sections = {
        '基础练习 (Ex 1-10)': [(n, t) for n, t in exercises if 1 <= int(n) <= 10],
        '进阶练习 (Ex 11-20)': [(n, t) for n, t in exercises if 11 <= int(n) <= 20],
        '函数练习 (Ex 21-30)': [(n, t) for n, t in exercises if 21 <= int(n) <= 30],
        '条件和循环 (Ex 31-40)': [(n, t) for n, t in exercises if 31 <= int(n) <= 40],
        '面向对象编程 (Ex 41-52)': [(n, t) for n, t in exercises if 41 <= int(n) <= 52],
    }

    for section_name, section_exercises in sections.items():
        if section_exercises:
            summary_content += f"## {section_name}\n"
            for ex_num, ex_title in section_exercises:
                summary_content += f"* [练习{ex_num}: {ex_title}](docs/ex{ex_num}.md)\n"
            summary_content += "\n"

    # 写入SUMMARY.md
    with open('SUMMARY.md', 'w', encoding='utf-8') as f:
        f.write(summary_content)

    print("✓ 已生成 SUMMARY.md")

if __name__ == '__main__':
    main()
