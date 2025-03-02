#!/usr/bin/python3
"""
Deploy web static archive
fab -f 3-deploy_web_static.py deploy -i my_ssh_private_key -u ubuntu
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa' aftee hosts
"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['52.207.208.233', '35.153.33.171']


def do_pack():
        """
        Function to compress directory
        """
        now = datetime.now()
        now = now.strftime('%Y%m%d%H%M%S')
        archive_path = 'versions/web_static_' + now + '.tgz'

        local('mkdir -p versions/')
        result = local('tar -cvzf {} web_static/'.format(archive_path))

        if result.succeeded:
                return archive_path
        return None


def do_deploy(archive_path):
        """
        Deploy web files to server
        """
        try:
                if not (path.exists(archive_path)):
                        return False

                put(archive_path, '/tmp/')

                timestamp = archive_path[-18:-4]
                run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

                run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
                    .format(timestamp, timestamp))

                run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

                run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

                run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
                    .format(timestamp))

                run('sudo rm -rf /data/web_static/current')

                run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))
        except:
                return False

        return True


def deploy():
        """
        Deploy web static
        """
        return do_deploy(do_pack())
