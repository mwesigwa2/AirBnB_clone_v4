#!/usr/bin/python3
from fabric.api import env, put, run
import os

env.hosts = ['100.25.34.61', '100.25.180.211']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """Deploy archive to web servers"""

    if not os.path.exists(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        archive_name = os.path.splitext(archive_filename)[0]

        # Upload the archive to the /tmp/ directory of the web servers
        put(archive_path, '/tmp/')

        # Create the release directory
        release_path = '/data/web_static/releases/{}'.format(archive_name)
        run('sudo mkdir -p {}'.format(release_path))

        # Uncompress the archive into the release directory
        run('sudo tar -xzf /tmp/{} -C {}'.format(archive_filename, release_path))

        # Delete the uploaded archive from the web servers
        run('sudo rm /tmp/{}'.format(archive_filename))

        # Remove the current symbolic link if it exists
        current_link = '/data/web_static/current'
        run('sudo rm -rf {}'.format(current_link))

        # Create a new symbolic link to the new version
        run('sudo ln -s {} {}'.format(release_path, current_link))

        return True

    except Exception as e:
        return False
