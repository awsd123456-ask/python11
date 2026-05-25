# 练习3: 数字和数学计算

## 代码示例

```python
#coding:utf-8
print "I will count my chickens:"# 我要数数我的鸡

print u"Hens， 母鸡",25+30 / 6
print u"Roosters, 公鸡",100-25*3%4

print u"Now I will count the eggs:（现在我要数鸡蛋了:）"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print  3 + 2 < 5 - 7

print "What is  3 + 2?",3 + 2
print "What is  5 - 7?",5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?",5 > -2
print "Is it greater or equal?",5 >= -2
print "Is it less or equal?",5 <= -2
```

## 学习笔记

### 1. 注释技巧
- 写注释的时候最好像示例这样写
- 利用快捷键 `Ctrl+D` 多复制几行

### 2. 输出格式
- 输出后面加计算要记得加逗号 `,`
```python
print "20 / 3 =",20 / 3
```

### 3. 浮点数概念
注意整数除法和浮点数除法的区别：
```python
print "20 / 3 =",20 / 3      # 结果: 6
print "20.0 / 3 =",20.0 / 3  # 结果: 6.666...
```

### 4. 除法计算结果
```python
print "7 / 6 < 7.0 / 6.0",7 / 6 < 7.0 / 6.0  # True
```
- 整数除法会向下取整
- 浮点数除法会保留小数

## 运行结果

```
I will count my chickens:
Hens， 母鸡 30
Roosters, 公鸡 97
Now I will count the eggs:（现在我要数鸡蛋了:）
7
Is it true that 3 + 2 < 5 - 7?
False
What is  3 + 2? 5
What is  5 - 7? -2
Oh, that's why it's False.
How about some more.
Is it greater? True
Is it greater or equal? True
Is it less or equal? False
```
