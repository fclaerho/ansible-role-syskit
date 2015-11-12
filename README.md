
<!-- THIS IS A GENERATED FILE, DO NOT EDIT -->

System Integration Kit. Finish integrating services and tools by configuring system specific features such as users, firewall, proxies, logs, etc. See the usage section for the exhaustive list of configurable features.
 Version 0.1.


## Supported Platforms

  * Ubuntu
  * Debian

## Variables

| Name | Value | Description |
|------|-------|-------------|
| syskit_ferm_modules | _(default:)_ [] | List of dict {'name', ['daddr'], ['proto'], ['dport']} |
| syskit_logrotate_modules | _(default:)_ [] | List of dict {'name', 'path', 'size', 'rotate'} |
| syskit_users | _(default:)_ [] | List of dict {'name', 'home', 'groups', 'state', 'sshkeys': {'name', 'keyval', 'pubval'}…} |



## Usage

To use this role from a **playbook**, 
register its ID in the project `requirements.{txt,yml}` file.
To add this role as another **role dependency**,
register its ID in the `dependencies` list of the role manifest `meta/main.yml`.
For further details,
please refer to the Ansible documentation at https://docs.ansible.com/playbooks_roles.html.

The integration work is typically done at the playbook level: use 3rd-party roles to provision tools and services then set `syskit_*` variables to configure the system features.
Configurable features:
  * Log Management: logrotate
  * Firewalling: [Ferm](http://ferm.foo-projects.org)
  * Users: create/delete accounts, install SSH keys



## Maintenance

Install [ansible-universe](https://github.com/fclaerho/ansible-universe)
and run `ansible-universe check` to re-generate this distribution.

The following files are generated or updated based on various role assets:
  * tasks/main.yml
  * README.md


