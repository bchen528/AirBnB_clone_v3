#!/usr/bin/python3
"""
Fabric script generates .tgz archive of all in web_static/ using function 'do_pack'
Usage: fab -f 1-pack_web_static.py do_pack

All files in the folder web_static must be added to the final archive
All archives must be stored in the folder versions (your function should create this folder if it doesn’t exist)
The name of the archive created must be web_static_<year><month><day><hour><minute><second>.tgz
The function do_pack must return the archive path if the archive has been correctly generated. Otherwise, it should return None
"""
from fabric.api import local
from time import strftime


def do_pack():
    """generate .tgz archive of web_static/ folder"""
    timenow = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_{}".format(timenow)
        local("tar -cvzf {} web_static/".format(filename))
        return filename
    except:
        return None
