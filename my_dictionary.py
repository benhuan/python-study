# coding=utf-8
# -*- coding: utf-8 -*-
__author__ = 'longqi'
'''
每一个元素是pair，包含key、value两部分。key是Integer或string类型，value
是任意类型。
键是唯一的，字典只认最后一个赋的键值。
'''
# dictionary的方法

D = {'ob1': 'computer', 'ob2': 'mouse', 'ob3': 'printer'}

print(D.get('ob1', 0))  # 同dict[key]，多了个没有则返回缺省值，0。[]没有则抛异常
print('ob4' in D)  # 有该键返回TRUE，否则FALSE
print(list(D.keys()))  # 返回字典键的列表
print(list(D.values()))  # 以列表的形式返回字典中的值，返回值的列表中可包含重复元素
print(list(D.items()))  # 将所有的字典项以列表方式返回，这些列表中的每一项都来自于(键,值),但是项在返回时并没有特殊的顺序

'''
D.update(dict2)  # 增加合并字典
D.popitem()  # 得到一个pair，并从字典中删除它。已空则抛异常
D.clear()  # 清空字典，同del dict
D.copy()  # 拷贝字典
D.cmp(dict1, dict2)  # 比较字典，(优先级为元素个数、键大小、键值大小)
# 第一个大返回1，小返回-1，一样返回0

#dictionary的复制
dict1 = dict  #别名
dict2 = dict.copy()  #克隆，即另一个拷贝。
'''
