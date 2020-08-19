# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:01:43 2020

@author: user
"""

from mcpi.minecraft import Minecraft

mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

BT=int(input("請輸入ID: "))
l=int(input("請輸入長度: "))
w=int(input("請輸入寬度: "))
h=int(input("請輸入高度: "))
mc.setBlocks(x,y,z,x+l,y+h,z+w,BT)

mc.setBlocks(x+1,y,z+1,x+l-1,y+h-1,z+w-1,0)

mc.setBlock(x+1,y,z,x+1,y+1,z,0)

mc.setBlocks(x+1,y+h-2,z+1,x+l-1,y+h-2,z+w-1,169)

a=4
while a<h:
    mc.setBlocks(x+1,y+a,z+1,x+l-1,y+a,z+w-1,169)
    mc.setBlocks(x+2,y+a,z+2,x+l-2,y+a,z+w-2,0)
    a=a+4