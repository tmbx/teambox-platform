#!/usr/bin/python

# This script mounts the cdrom disk if it is present and executes the
# bootstrap bundle from it.

from kfile import *
from krun import *

# CDROM device.
dev_cdrom = "/dev/cdrom"

# CDROM mount point.
cdrom_mp = "/media/cdrom/"

# Name of the bootstrap bundle when expanded. Add '.tgz' to get the tarball
# name.
bootstrap_bundle_name = "bs"

# Name of the script to execute.
bootstrap_script_name = "update.py"

def main():
    cdrom_bundle_path = cdrom_mp + bootstrap_bundle_name + ".tgz"
    
    # Change the directory to '/'.
    os.chdir("/");
    
    # Try to mount the CDROM disk.
    try: show_cmd_output(["mount", dev_cdrom])
    except:
        print("No CDROM disk present.")
        return
    
    # No bootstrap bundle.
    if not os.path.isfile(cdrom_bundle_path):
        print("%s is not present." % (cdrom_bundle_path))
        return
    
    # Expand the bundle.
    show_cmd_output(["tar", "-zxvf", cdrom_bundle_path])
    
    # Execute the bootstrap script.
    os.chdir(bootstrap_bundle_name)
    show_cmd_output(["./" + bootstrap_script_name])
    
main()

