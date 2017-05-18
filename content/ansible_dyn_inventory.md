Title: Ansible Dynamic Inventory Example
Date: 2017-05-12 12:03
Modified: 2017-05-12 12:03
Category: ansible, linux, rhel, centos
Tags: ansible, linux
Slug: ansible-dynamic-inventory-example
Authors: Abhijeet Kasurde
Summary: Example of Ansible Dynamic Inventory


```
#!/usr/bin/env python
import argparse
import json

ANSIBLE_INV = {
    "dbserver": {
        "hosts": ["10.65.100.10"],
        "vars": {
            "ansible_password": "Secret1234",
            "ansible_user": "devops",
        }
    },
}

def output_list_inventory(json_output):
    print json.dumps(json_output)

def main():

    # Argument parsing
    parser = argparse.ArgumentParser(description="Ansible dynamic inventory")
    parser.add_argument("--list", help="Ansible inventory of all of the groups",
        action="store_true", dest="list_inventory")
    parser.add_argument("--host",
        help="Ansible inventory of a particular host", action="store",
        dest="ansible_host", type=str)

    cli_args = parser.parse_args()
    list_inventory = cli_args.list_inventory
    ansible_host = cli_args.ansible_host

    if list_inventory:
        output_list_inventory(ANSIBLE_INV)


if __name__ == "__main__":
    main()

```
