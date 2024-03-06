#!/usr/bin/python3
"""Distributes an archive to my web servers"""


from fabric.api import env, put, run
import os

env.hosts = ['100.24.244.220', '34.239.250.31']


def do_deploy(archive_path):
    """Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    """
    if not os.path.exists(archive_path):
        return False

    filename = os.path.basename(archive_path)
    folder_name = filename.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    res = False

    try:
        put(archive_path, '/tmp/')
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(filename, folder_path))
        run("rm -rf /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('Deployed!')
        res = True
    except Exception:
        res = False
    return res
