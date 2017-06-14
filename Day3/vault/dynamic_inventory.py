#!/usr/bin/env python


import argparse
import subprocess
import json
from os.path import expanduser

def dm(*args):
    return subprocess.check_output(["docker"] + list(args)).strip()

def dminspect(fmt, mcn):
    return dm("inspect", "-f", fmt, mcn)

def dmport(machine):
    output = dm("port", machine, "22") 
    return output[8:]

def get_host_and_vars(m):
    home = expanduser("~") 
    hosts = [dminspect("{{.NetworkSettings.IPAddress}}", m)]
    ssh_vars = {
         "ansible_ssh_port": dmport(m),
         "ansible_ssh_host": "localhost",
         "ansible_ssh_private_key_file": home+ "/.ssh/" + "id_rsa",
         "ansible_ssh_user": "root",
         "ansible_ssh_password": "root",
         "ansible_become_user": "root",
         "ansible_become_password": "root"
    }
    data = {"hosts": hosts, "vars": ssh_vars}
    return data

class DockerMachineInventory(object):
      def __init__(self):
          self.inventory = {} # Ansible Inventory

          parser = argparse.ArgumentParser(description='Produce an Ansible Inventory file based on Docker Machine status')
          parser.add_argument('--list', action='store_true', help='List all active Droplets as Ansible inventory (default: True)')
          self.args = parser.parse_args()

          machines = dm("ps", "-q").splitlines()
          json_data = {m: get_host_and_vars(m) for m in machines}

          print json.dumps(json_data)

DockerMachineInventory()
