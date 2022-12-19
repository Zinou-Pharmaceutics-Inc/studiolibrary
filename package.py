# -*- coding: utf-8 -*-

name = 'studiolibrary'

version = '2.9.6.b3_hik'

requires = ['maya']

private_build_requires = ['rezutil-1']
build_command = "python -m rezutil build {root}"

def commands():
    global env
    
    env.PYTHONPATH.append("{root}/src")
