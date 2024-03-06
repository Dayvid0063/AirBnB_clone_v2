#!/usr/bin/python3
"""Deletes out-of-date archives"""


import os
from fabric.api import *


env.hosts = ["100.24.244.220", "34.239.250.31"]


def do_clean(number=0):
    """Out-of-date archives removed"""
    number = 1 if int(number) == 0 else int(number)
    record = sorted(os.listdir("versions"))
    [record.pop() for u in range(number)]

    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in record]

    with cd("/data/web_static/releases"):
        record = run("ls -tr").split()
        record = [a for a in record if "web_static_" in a]
        [record.pop() for u in range(number)]
        [run("rm -rf ./{}".format(a)) for a in record]
