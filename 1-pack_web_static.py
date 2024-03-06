#!/usr/bin/python3
"""Generates .tgz archive from contents of the web_static folder"""


from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """Creates a .tgz archive"""
    dt_stamp = datetime.utcnow()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        dt_stamp.year,
        dt_stamp.month,
        dt_stamp.day,
        dt_stamp.hour,
        dt_stamp.minute,
        dt_stamp.second
    )

    if not os.path.exists('versions'):
        os.makedirs('versions')

    res = local("tar -cvzf {} web_static".format(output))
    if res.failed:
        return None

    return output
