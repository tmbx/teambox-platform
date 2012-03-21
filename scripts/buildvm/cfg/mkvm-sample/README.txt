This is a sample configuration to deploy a VM or a set of VM on a ESXi host.

===========================================================
If you are going to deploy a single VM:

- Copy this directory.
- Edit config.ini.
- Edit master.py if you are deploying a configured VM.
- Execute 'mkvm'.


===========================================================
If you are going to deploy a set of VMs:

- Copy this directory.
- Edit config.ini but do not enter VM-specific data.
- Edit master.py but do not enter VM-specific data.

- For each VM:
  - Clone this directory.
  - Edit config.ini.
  - Edit master.py and enter the VM-specific data.
  - Execute 'mkvm'.

Alternatively, you could just clone master.py once per VM and modify config.ini
in the same directory.

DO NOT EXECUTE 'mkvm' CONCURRENTLY IN THE SAME DIRECTORY.

