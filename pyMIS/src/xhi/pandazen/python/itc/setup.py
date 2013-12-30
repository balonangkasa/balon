'''
Created on Dec 19, 2013

@author: pandazen
'''
from cx_Freeze import setup, Executable

exe = Executable(
    script="fmbfmxcmp.py",
    base="Win32GUI",
    )
 
setup(
    name = "compareFMBvsFMX",
    version = "0.1",
    description = "compare FMB vs FMX",
    executables = [exe]
    )