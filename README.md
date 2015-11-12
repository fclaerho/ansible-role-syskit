
<!-- THIS IS A GENERATED FILE, DO NOT EDIT -->

System Integration Kit. Finish integrating services and tools by configuring system specific features such as users, firewall, proxies, logs, etc. See the usage section of the exhaustive list of configurable features.
 Version 0.1.


## Supported Platforms

  * Ubuntu
  * Debian

## Variables

| Name | Value | Description |
|------|-------|-------------|
| debkit_ferm_modules | _(default:)_ [] | List of dict {'name', ['daddr'], ['proto'], ['dport']} |
| debkit_logrotate_modules | _(default:)_ [] | List of dict {'name', 'path', 'size', 'rotate'} |
| debkit_users | _(default:)_ [] | List of dict {'name', 'home', 'groups', 'state', 'sshkeys': {'name', 'keyval', 'pubval'}…} |



## Usage

To use this role from a **playbook**, 
register its ID in the project `requirements.{txt,yml}` file.
To add this role as another **role dependency**,
register its ID in the `dependencies` list of the role manifest `meta/main.yml`.
For further details,
please refer to the Ansible documentation at https://docs.ansible.com/playbooks_roles.html.

Configurable features:
  * Logrotate
  * Users
  * [Ferm](), Debian default firewall abstraction


## Maintenance

Install [ansible-universe](https://github.com/fclaerho/ansible-universe)
and run `ansible-universe check` to re-generate this distribution.

The following files are generated or updated based on various role assets:
  * tasks/main.yml
  * README.md


