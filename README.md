
<!-- THIS IS A GENERATED FILE, DO NOT EDIT -->

Debian system integration kit. Configure users, groups, firewall, proxies, logs, etc. for services and tools.
 / Version 0.1.


## Supported Platforms

  * Ubuntu
  * Debian

## Variables

| Name | Value | Description |
|------|-------|-------------|
| debkit_users |   | List of dict {'name', 'home', 'groups', 'state', 'sshkeys': {'keyval', 'pubval', 'filename'}…} |



## Usage

To use this role from a **playbook**, 
register its ID in the project `requirements.{txt,yml}` file.
To add this role as another **role dependency**,
register its ID in the `dependencies` list of the role manifest `meta/main.yml`.
For further details,
please refer to the Ansible documentation at https://docs.ansible.com/playbooks_roles.html.




## Maintenance

Install [ansible-universe](https://github.com/fclaerho/ansible-universe)
and run `ansible-universe check` to re-generate this distribution.

The following files are generated or updated based on various role assets:
  * tasks/main.yml
  * README.md


