# 练习7: 更多打印

## 📝 练习目标

巩固练习输出，学习字符串重复和连接

## 💻 代码示例

```python
#coding:utf-8
print "Mary had a little lamb"# 羊羔
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."# 羊毛
# "."输出了十次
print "." * 10 # what 'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma(逗号) at the end. try removing it to see what happens
# 在下面一行加逗号输出结果：在一行，中间用一个空格隔开
# 不加逗号的结果：分别输出在两行
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
```

## 📚 作者学习笔记

- **字符串重复**: `"." * 10` 会输出10个点
- **逗号的作用**: 在 print 语句末尾加逗号，下一个 print 会在同一行输出，中间用空格隔开
- **不加逗号**: 两个 print 语句会分别输出在两行

## 🎯 初学者提示

### 重要概念
1. **字符串乘法**: `字符串 * 数字` 可以重复输出字符串
   ```python
   print "=" * 20  # 输出20个等号
   ```

2. **字符串连接**: 使用 `+` 号连接多个字符串
   ```python
   "Cheese" + "Burger"  # 结果: "CheeseBurger"
   ```

3. **print 末尾的逗号** (Python 2 特性):
   - 有逗号: 下一个 print 在同一行
   - 无逗号: 下一个 print 在新的一行

### 运行结果

```
Mary had a little lamb
Its fleece was white as snow.
And everywhere that Mary went.
..........
Cheese Burger
```

### 练习建议
- 尝试修改 `"." * 10` 中的数字，看看效果
- 试试去掉第一个 print 末尾的逗号，观察输出变化
- 用字符串乘法画一些简单的图案
