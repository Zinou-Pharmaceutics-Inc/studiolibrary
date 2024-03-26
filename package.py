# -*- coding: utf-8 -*-

name = 'studiolibrary'

version = '2.14.1'

requires = ['maya']

private_build_requires = ['rezutil-1']
build_command = "python -m rezutil build {root}"

def commands():
    global env

    env.PYTHONPATH.append("{root}/src")

    env.OPENSSL_ia32cap="~0x200000200000000"
