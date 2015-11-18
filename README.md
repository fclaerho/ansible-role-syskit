
<!-- THIS IS A GENERATED FILE, DO NOT EDIT -->

System Integration Kit. Integrate services and tools by configuring system specific concerns such as users, logging, services, reverse proxying, firewalling and so on. See the usage section for the exhaustive list of configurable concerns.
 Version 0.1.


## Supported Platforms

  * Debian
  * Ubuntu

## Variables

| Name | Value | Description |
|------|-------|-------------|
| `syskit_apt_proxy` | _default_ `None` | Dict {'http': {'hostname', ['directs']}, 'https': {'hostname', ['directs ']}} |
| `syskit_ferm_rules` | _default_ `[]` | List of dict {'name', ['daddr'], ['proto'], ['dport'], 'state': present/absent} |
| `syskit_logrotate_autopurge` | _default_ `False` | Boolean. Purge logrotate if no module is defined |
| `syskit_logrotate_modules` | _default_ `[]` | List of dict {'name', 'path', 'size', 'state': present/absent, 'rotate'} |
| `syskit_nginx_autopurge` | _default_ `True` | Boolean. Purge nginx if no site is defined |
| `syskit_nginx_sites` | _default_ `[]` | List of dict {'name', 'state': present/absent, 'enabled': yes/no, 'upstreams', 'servers'}. An **upstream** is a dict {'name', 'servers'}. A **server** is a dict {'name', 'port', ['default'], 'tls': [{'crtpath', 'keyval'}], 'locations'}. An **upstream.server** is a dict {'address', 'port', ['weight'], ['max_fails'], ['fail_timeout'], ['backup'], ['down'], ['max_conns'], ['resolve'], ['route'], ['slow_start']}. A **location** is a dict {['uri'=/], ('root', ['autoindex'=off], ['expires']) or ('proxy_pass', ['client_max_body_size'])}. |
| `syskit_root_pw_locked` | _default_ `False` | Boolean. If set, lock root password (recommended) |
| `syskit_sysv_manifests` | _default_ `[]` | List of dict {'uid', 'name', 'argv', 'state': present/absent, 'daemon', ['pidfile'], 'description'} |
| `syskit_sysv_manifests_path` | _var_ `/etc/init.d` |  |
| `syskit_upstart_manifests` | _default_ `[]` | List of dict {'uid', 'name', 'argv', 'state': present/absent, 'daemon', 'description'} |
| `syskit_upstart_manifests_path` | _var_ `/etc/init` |  |
| `syskit_users` | _default_ `[]` | List of dict {'name', 'home', 'groups', 'state': present/absent, 'sudoer': yes/no, 'sshkeys': {'name', 'keyval', 'pubpath', 'state': present/absent}…, 'authorized_keys': {'val', 'state': present/absent}…} |



## Usage

To use this role from a **playbook**, 
register its ID in the project `requirements.{txt,yml}` file.
To add this role as another **role dependency**,
register its ID in the `dependencies` list of the role manifest `meta/main.yml`.
For further details,
please refer to the Ansible documentation at https://docs.ansible.com/playbooks_roles.html.

This role is registered on [Galaxy](https://galaxy.ansible.com/detail#/role/6063)
with the ID `fclaerho.syskit`.

The integration work is typically done at the playbook level:
use 3rd-party roles to provision tools and services then
set `syskit_*` variables to configure the system concerns.

Configurable concerns:

  * **Reverse Proxying**: create/delete/update vhosts
    * [Nginx](http://nginx.org/en/) — `syskit_nginx_*`
  * **Firewalling**: create/delete/update rules
    * [Ferm](http://ferm.foo-projects.org) — `syskit_ferm_rules`
  * **Services**: create/delete/update manifests
    * [Upstart](http://upstart.ubuntu.com/cookbook/) — `syskit_upstart_manifests`
    * [SysV](https://en.wikipedia.org/wiki/Init#SysV-style) — `syskit_sysv_manifests`
  * **Logging**:
    * Redirection: #TODO
    * Rotation: [Logrotate](http://www.linuxcommand.org/man_pages/logrotate8.html) — `syskit_logrotate_*`
  * **Users**: create/delete/update accounts — `syskit_users`
  * **Misc**:
    * Lock/Unlock the root account — `syskit_root_pw_locked`
    * Configure Apt proxy — `syskit_apt_proxy`

**NOTICE:** All private keys `*.keyval` are expected to be securely stored via [Ansible-vault](http://docs.ansible.com/ansible/playbooks_vault.html) (or any equivalent.) Public assets (certificates `*.crtpath`, public keys `*.pubpath`) are expected to be files copied over.



## Maintenance

Install [ansible-universe](https://github.com/fclaerho/ansible-universe)
and run `ansible-universe check` to re-generate this distribution.

The following files are generated or updated based on various role assets:

  * `tasks/main.yml`
  * `README.md`

On [Galaxy](https://galaxy.ansible.com/accounts/profile), re-import the repository.

