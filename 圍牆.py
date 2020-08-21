# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 10:14:09 2020

@author: user
"""

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x,y,z=mc.player.getPos()

l=int(input("請輸入長度: "))
w=int(input("請輸入寬度: "))

mc.setBlocks(x,y,z,x+l,y+3,z+w,98)
mc.setBlocks(x+1,y,z+1,x+l-1,y+3,z+w-1,0)