# 练习9: 打印，打印，打印

## 📝 练习目标

学习换行符和多行字符串的使用

## 💻 代码示例

```python
#coding:utf-8
# Here's some new strange stuff,remember type it exactly.
# (这是一些新的奇怪的东西)

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days:", days
print "Here are the months:", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
```

## 📚 作者学习笔记

- **\n 是换行符**: 在字符串中插入换行
- **三引号字符串**: 三个双引号 `"""` 包含的内容可以是多行存在的
- **代码风格**: 少用 `""""""` 这个不优雅（作者建议）

## 🎯 初学者提示

### 重要概念

1. **转义字符 \n**
   - `\n` 表示换行
   - 在字符串中任意位置插入换行
   ```python
   print "第一行\n第二行\n第三行"
   ```

2. **多行字符串（三引号）**
   - 使用 `"""` 或 `'''` 包裹
   - 可以直接换行，不需要 \n
   - 保留所有格式（包括缩进和空行）

3. **两种方式的对比**
   ```python
   # 方式1: 使用 \n
   text1 = "第一行\n第二行\n第三行"
   
   # 方式2: 使用三引号
   text2 = """
   第一行
   第二行
   第三行
   """
   ```

### 运行结果

```
Here are the days: Mon Tue Wed Thu Fri Sat Sun
Here are the months: Jan
Feb
Mar
Apr
May
Jun
Jul
Aug

There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.

```

### 练习建议
- 尝试在不同位置添加 \n，观察效果
- 用三引号写一首小诗或一段文字
- 比较 `"""` 和 `'''` 的使用（功能相同）
- 注意三引号字符串会保留所有空格和换行
