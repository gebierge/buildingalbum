# !/user/bin/env python3.7
# -*- coding:utf-8 -*-
# @Time     : 2019/12/5 8:28 下午
# @Author   : Baochang liu
# @User     : gj
# @File     : AlbumGenerater.py
# @Software : PyCharm

import os

# 楼幢列表
floor_list1 = ['7幢', '8幢', '9幢', '10幢', '11幢', '12幢']
floor_list2= ['13幢', '14幢']
# 单元列表
unit_code = ['1单元', '2单元']

# 读取7、8、9、10、11、12号楼工序节点
with open('optnode7.txt') as opt7:
    operation_node7 = opt7.readlines()

# 读取13、14号楼工序节点
with open('optnode13.txt') as opt13:
    operation_node13 = opt13.readlines()

def RoomNumOptAlbum(floor_list, unitcode, range_s, range_e, operation_node):
    for fl in floor_list:
        for uc in unitcode:
            for floor in range(range_s,range_e):    # 设置楼层起止数
                roomnum = []
                if uc == "1单元":    # 设置单元房号序列起止数
                    range_start = 1
                    range_end = 3
                else:
                    range_start = 3
                    range_end = 5
                for n in range(range_start,range_end):
                    rnum = str(floor)+str(0)+str(n)    # 拼接房号
                    rnum.strip()
                    roomnum.append(rnum)    # 保存单元单层房号
                for ronum in roomnum:
                    for opn in operation_node:    # 遍历该楼栋工序节点
                        os.makedirs(r"{0}/{1}/{2}/{3}".format(fl, uc,ronum, opn))    # 生成楼幢房号及节点相册目录

# 生成7-12号楼每户节点相册
RoomNumOptAlbum(floor_list1, unit_code, 2, 31, operation_node7)


# 生成13、14号楼每户节点相册
RoomNumOptAlbum(floor_list2, unit_code, 1, 23, operation_node13)