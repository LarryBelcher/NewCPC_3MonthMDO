#!/usr/bin/python

import os, subprocess


cmd = "rm /work/NewCPC_3MonthMDO/sdo_polygons*"
subprocess.call(cmd,shell=True)

cmd = "rm /work/NewCPC_3MonthMDO/Drought--ThreeMonth--Drought-Outlook--US--*.png"
subprocess.call(cmd,shell=True)


cmd = "rm /work/NewCPC_3MonthMDO/Data/*"
subprocess.call(cmd,shell=True)
