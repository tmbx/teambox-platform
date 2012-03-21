import sys; sys.path.append("/teambox"); from kasmodel import *

# Uncomment and change values as needed.
def setup(root, eth0):
    
    # Administration and root password. The default is empty.
    root.admin_pwd = ""
    
    # Private host name of the machine without the domain. The default is
    # localhost.
    root.hostname = ""
    
    # Private domain name of the machine. The default is empty.
    root.domain = ""
    
    # Public host names. The default is empty.
    root.kcd_host = ""
    root.kwmo_host = ""
    
    # List of IP addresses of the form X.X.X.X/X that have access to all ports
    # of this server. The default is every address.
    root.all_port_addr_list = [ "0.0.0.0/0" ]
    
    # List of IP addresses of the form X.X.X.X/X that have accesss to the
    # configuration ports of this server. The default is every address.
    root.config_port_addr_list = [ "0.0.0.0/0" ]
                           
    # List of custom lines to insert into /etc/ssh/sshd_config.
    root.sshd_line_list = []
    
    # For static IP. The default is DHCP.
    #eth0.method = "static"
    #eth0.ip = ""
    #eth0.netmask = ""
    #eth0.gateway = ""
    
    # DNS server addresses. Leave empty if using DHCP.
    #root.dns_addr_list = []
    
    
    ############################################################
    ### CLONE HERE UNLESS YOU HAVE ONLY ONE MACHINE TO SETUP ###
    ############################################################
    
    
    ### TBXSOS, FREEMIUM AND WPS SERVICES ###
    
    # Enable the service. The default is disabled.
    #root.tbxsos_service = 1
    
    # Enable the service. The default is disabled.
    #root.freemium_service = 1
    
    # True if the users are allowed to auto-register. The default is disabled.
    #root.freemium_autoregister = 1
    
    # Enable the service. The default is disabled.
    #root.wps_service = 1
    
    
    ### MAS SERVICE ###
    
    # Enable the service. The default is disabled.
    #root.mas_service = 1
    
    # Enable restrictions. The default is disabled.
    #root.kcd_enforce_restriction = 1
    
    # Organizations. The default is empty.
    #root.kcd_organizations[20000] = "Opersys"
    
    # Default KFS quota, in megabytes. The default is 10240.
    #root.kcd_default_kfs_quota = 10240
    
    # Mail information.
    #root.kcd_mail_host = "mail"
    #root.kcd_mail_sender = ""
    #root.kcd_mail_auth_user = ""
    #root.kcd_mail_auth_pwd = ""
    #root.kcd_mail_auth_ssl = 0

# Load and update master.cfg.
def main():
    root = RootConfigNode()
    root.load_master_config("master.cfg", update=1)
    setup(root, root.eth0)
    root.save_master_config("master.cfg")

main()

