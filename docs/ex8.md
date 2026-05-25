# 练习8: 打印，打印

## 📝 练习目标

学习使用格式化字符串模板，巩固 %r 的使用

## 💻 代码示例

```python
#coding:utf-8
formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
```

## 📚 作者学习笔记

- **%r 的原理**: 代表的字符串中有单引号 `'`，就自动加双引号 `"`
- **格式化模板**: 可以创建一个全是格式化字符串的字符串，来规范输出格式
- **中文输出**: 如果输出的是中文请用 `%s`，不要用 `%r`
  ```python
  print formatter % (u"我",u"是",u"小",u"寒")
  ```

## 🎯 初学者提示

### 重要概念

1. **格式化模板的复用**
   - 定义一次格式，多次使用
   - `formatter = "%r %r %r %r"` 定义了4个占位符的模板

2. **%r 的智能引号**
   - 自动选择单引号或双引号
   - 显示数据的原始形式（调试用）

3. **多行格式化**
   - 可以用括号包裹多行参数
   - 提高代码可读性

### 运行结果

```
1 2 3 4
'one' 'two' 'three' 'four'
True False False True
'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'
```

### 练习建议
- 创建不同数量占位符的格式化模板
- 观察 %r 如何处理不同类型的数据
- 尝试混合使用 %r 和 %s，比较区别
- 注意最后一行输出中引号的变化规律
