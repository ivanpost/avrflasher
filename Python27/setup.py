#!/usr/bin/python2.7
from cx_Freeze import setup, Executable

setup(
    name = "Aquaflash",
    version = "0.1",
    description = "Aquarius flash",
    executables = [Executable("Aurllib22.py")]
)
