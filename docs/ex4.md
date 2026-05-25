# 练习4: 变量和命名

## 代码示例

```python
#coding:utf-8
# 变量就像名字，用来方便的代表某个东西

# 汽车有100
# 每辆车能坐4个人
# 有30个司机
# 乘客90人
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_drvien = cars - drivers  # 有车没司机的数量
cars_driven = drivers             # 有车有司机的数量
carpool_capacity = cars_driven * space_in_a_car  # 所有能走的车加起来座位的数量
average_passengers_per_car = passengers / cars_driven  # 每辆车几个人

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_drvien, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
```

## 学习笔记

- **变量的作用**: 变量就像名字，用来方便地代表某个东西
- **变量命名**: 使用有意义的变量名，如 `cars`、`drivers`、`passengers`
- **浮点数计算**: 如果计算式子中有浮点数，结果必然为浮点数
  ```python
  print "4.0 + 3=", 4.0 + 3  # 结果: 7.0
  ```

## 运行结果

```
There are 100 cars available.
There are only 30 drivers available.
There will be 70 empty cars today.
We can transport 120.0 people today.
We have 90 to carpool today.
We need to put about 3 in each car.
```
