
<!-- THIS IS A GENERATED FILE, DO NOT EDIT -->

System Integration Kit. Integrate services and tools by configuring system specific concerns such as logs, users, services, firewalling, proxying and so on. See the usage section for the exhaustive list of configurable concerns.
 Version 0.1.


## Supported Platforms

  * Ubuntu
  * Debian

## Variables

| Name | Value | Description |
|------|-------|-------------|
| syskit_ferm_modules | _(default:)_ [] | List of dict {'name', ['daddr'], ['proto'], ['dport'], 'state'} |
| syskit_logrotate_modules | _(default:)_ [] | List of dict {'name', 'path', 'size', 'state', 'rotate'} |
| syskit_sysv_manifests | _(default:)_ [] | List of dict {'uid', 'name', 'argv', 'state', 'daemon', ['pidfile'], 'description'} |
| syskit_sysv_manifests_path | _(var:)_ /etc/init.d | None |
| syskit_upstart_manifests | _(default:)_ [] | List of dict {'uid', 'name', 'argv', 'state', 'daemon', 'description'} |
| syskit_upstart_manifests_path | _(var:)_ /etc/init | None |
| syskit_users | _(default:)_ [] | List of dict {'name', 'home', 'groups', 'state', 'sshkeys': {'name', 'keyval', 'pubval'}…} |



## Usage

To use this role from a **playbook**, 
register its ID in the project `requirements.{txt,yml}` file.
To add this role as another **role dependency**,
register its ID in the `dependencies` list of the role manifest `meta/main.yml`.
For further details,
please refer to the Ansible documentation at https://docs.ansible.com/playbooks_roles.html.

The integration work is typically done at the playbook level: use 3rd-party roles to provision tools and services then set `syskit_*` variables to configure the system concerns.
Configurable concerns:
  * Log Management: [Logrotate](http://www.linuxcommand.org/man_pages/logrotate8.html)
  * Firewalling: create/delete rules
    * [Ferm](http://ferm.foo-projects.org)
  * Services: create/delete manifests
    * [Upstart](http://upstart.ubuntu.com/cookbook/)
    * [SysV](https://en.wikipedia.org/wiki/Init#SysV-style)
  * Users: create/delete accounts, install SSH keys



## Maintenance

Install [ansible-universe](https://github.com/fclaerho/ansible-universe)
and run `ansible-universe check` to re-generate this distribution.

The following files are generated or updated based on various role assets:
  * tasks/main.yml
  * README.md


