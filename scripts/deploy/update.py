#!/usr/bin/python

# This script is executed to automatically configure a fresh K2 VM once it has
# been created and booted.

from kfile import *
from krun import *
from kasmodel import *

# Delete the path specified recursively.
def rm_path(path):
    show_cmd_output(["rm", "-rf", path])

# Perform a recursive copy of 'src' to 'dst'. 'src' is assumed to be a shell
# pattern.
def rec_copy(src, dst):
    show_cmd_output("cp -r %s %s" % (src, dst), shell_flag=1)

def main():
    
    # Read the VM name.
    vm_name = read_file("vm_name").strip()
    
    # Read the action file.
    action = read_file("action").strip()
    
    # Configure the machine for DHCP.
    if action == "dhcp":
        show_cmd_output(["/update/ifup", vm_name])
    
    # Install the Teambox software.
    if action == "conf" or action == "dist":
        
        # Load the configuration.
        service_manager = ServiceManager()
        root_cfg = RootConfigNode()
        root_cfg.load_master_config("master.cfg")
        
        # Set the root password before starting the network.
        root_cfg.set_root_pwd()
        
        # Setup the network.
        root_cfg.write_etc_hostname_file()
        root_cfg.write_etc_hosts_file()
        root_cfg.write_etc_network_file()
        root_cfg.write_etc_resolv_file()
        service_manager.reload_hostname()
        service_manager.reload_network_iface()
        
        # Read the bootstrap args.
        if os.path.isfile("bootstrap_args"): bootstrap_args = read_file("bootstrap_args").split()
        else: bootstrap_args = []
        
        # Run the bootstrap script.
        show_cmd_output(["./bootstrap.sh"] + bootstrap_args)
        
    # Configure the machine.
    if action == "conf":
        show_cmd_output("/etc/init.d/regencerts.sh start")
        show_cmd_output("/etc/init.d/sethostkeys.sh start")
        show_cmd_output("/etc/init.d/ssh restart")
        show_cmd_output("cp -f master.cfg /etc/teambox/base")
        show_cmd_output("chmod 666 /etc/teambox/base/master.cfg")
        
        root_cfg.set_admin_pwd()
        root_cfg.switch_to_production_mode(service_manager)
    
    sys.stdout.write("\n\nMachine setup complete.\n")
       
    # Flush the streams before we send the email.
    sys.stdout.flush()
    sys.stderr.flush()
    
    # Send the email.
    if os.path.isfile("email_recs"):
        email_recs = read_file("email_recs").split()
        s = ""
        s += "From: no-reply@teambox.co\n"
        s += "To: %s\n" % (", ".join(email_recs))
        s += "Subject: %s is ready\n" % (vm_name)
        s += "\n"
        s += read_file("/update/update.log")
        write_file("mail.txt", s)
        show_cmd_output("ssmtp -C ssmtp.conf %s < mail.txt" % (" ".join(email_recs)), shell_flag=1)
    
    # Clean up leftovers.
    rm_path("/etc/rc2.d/S99nextboot")
    rm_path("/update")
    rm_path("/k2_sys.tar.gz")
    rm_path("/k2_sys")
    rm_path("/oldsys")
    rm_path("/bs")
    rm_path("/bs.tar.gz")
    
    # Shut down the machine.
    if action == "dist":
        show_cmd_output("init 0")
    
main()

