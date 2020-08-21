# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 10:14:09 2020

@author: user
"""

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x,y,z=mc.player.getPos()

mc.setBlocks(x,y,z,x+50,y+3,z+50,98)
mc.setBlocks(x+1,y,z+1,x+49,y+3,z+49,0)