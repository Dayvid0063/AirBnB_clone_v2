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

    put(archive_path, '/tmp/')

    filename = os.path.basename(archive_path)
    dir_name = filename.replace(".tgz", "")
    dir_path = "/data/web_static/releases/{}/".format(dir_name)

    try:
        run("mkdir -p {}".format(dir_path))
        run("tar -xzf /tmp/{} -C {}".format(filename, dir_path))
        run("rm -rf /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(dir_path, dir_path))
        run("rm -rf {}web_static".format(dir_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(dir_path))
        print('Deployed!')
        return True
    except Exception:
        return False
