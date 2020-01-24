Title: VMware Core Info
Date: 2020-01-10 12:03
Modified: 2016-01-10 12:03
Category: vmware
Tags: vmware, ansible, automation, command line
Slug: vmware-core-info
Authors: Abhijeet Kasurde
Summary: Using Ansible to retrieve information about VMware objects


Module introduction - vmware_core_info

User can retrieve information about various VMware objects using Ansible. VMware has recently added REST APIs to communicate with vSphere. Ansible uses these APIs to perform automation related to VMware. In this article, we will be discussing `vmware_core_info` Ansible module, which allows user to retrieve information about VMware object.

main.yml
--------

```
---
- hosts: all
  gather_facts: no
  connection: httpapi
  vars:
    datacenter_name: Asia-Datacenter1
  vars_files:
    - vcenter_vars.yml
  tasks:
  - name: Get all Datacenter
    vmware_core_info:
      object_type: datacenter
    register: all_dcs

  - name: Get managed object id for datacenter
    set_fact:
      datacenter_managed_object_id: "{{ item.datacenter }}"
    loop: "{{ all_dcs.datacenter.value | json_query(dc_query) }}"
    vars:
      dc_query: "[?name == `{{ datacenter_name }}` ]"

  - name: Display MoID for datacenter
    debug:
      msg: "{{ datacenter_managed_object_id }}"

  - name: Get all ESXi information
    vmware_core_info:
      object_type: host
      filters:
        - datacenters: "{{ datacenter_managed_object_id }}"
    register: esxi_list

```

here, we are using Ansible VMware httpapi plugin to connect to vSphere REST API. You can read more about Ansible httpapi plugin [here](https://docs.ansible.com/ansible/latest/plugins/httpapi.html)

Using VMware httpapi connection plugin, we are first retrieving datacenter managed object for the given datacenter i.e. "Asia-Datacenter1". Once we have that, we use this value to filter ESXi hostsystems in the given VMware infrastructure.

You can find about vmware_core_info all options and details [here](https://docs.ansible.com/ansible/devel/modules/vmware_core_info_module.html)

You can get all the code for this example [here](https://github.com/Akasurde/ansible-reproducers/tree/master/blog/jan_2020)