
System integration kit — Integrate services and tools by configuring system specific concerns.

* * *

Usage
-----

This role is registered on Galaxy with the ID `fclaerho.syskit`.

- to use this role from a **playbook**, 
  add its ID to the project `requirements.{txt,yml}` file.
- to add this role as another **role dependency**,
  add its ID in the `dependencies` list of the role manifest `meta/main.yml`.

For further details,
please refer to the Ansible documentation at https://docs.ansible.com/playbooks_roles.html.

The integration work is typically done at the playbook level:
- use 3rd-party roles to provision tools and services
- then set `syskit_*` variables to configure the system concerns.

All private keys `*.keyval` should be securely stored via [Ansible-vault](http://docs.ansible.com/ansible/playbooks_vault.html) (or any equivalent.)

Supported platforms:
- D: Debian
- U: Ubuntu
- : macOS
- *: Any

Concerns
--------

### Users

Create/delete/update accounts.

| Platform | Name | Value | Description |
|----------|------|-------|-------------|
| * | `syskit_users` | _default_ `[]` | List of dict {'name', ['home'], ['shell': /bin/bash], 'state': present/absent, ['groups'], 'sudoer': yes/no, 'sshkeys': {'name', 'keyval', 'pubval', 'state': present/absent}…, 'authorized_keys': {'val', 'state': present/absent}…} |
| DU | `syskit_root_pw_locked` | _default_ `False` | Boolean. If set, lock root password (recommended) |


### Services

Create/delete/update service manifests.

[Upstart](http://upstart.ubuntu.com/cookbook/) — `syskit_upstart_manifests`
[SysV](https://en.wikipedia.org/wiki/Init#SysV-style) — `syskit_sysv_manifests`

| Platform | Name | Value | Description |
|----------|------|-------|-------------|
| D | `syskit_sysv_manifests` | _default_ `[]` | List of dict {'uid', 'name', 'argv', 'state': present/absent, 'daemon', ['pidfile'], 'description'} |
| U | `syskit_upstart_manifests` | _default_ `[]` | List of dict {'uid', 'name', 'argv', 'state': present/absent, 'daemon', 'description'} |


### Applications

| Platform | Name | Value | Description |
|----------|------|-------|-------------|
|  | `syskit_macosx_apps` | - | - |


### Package Management

Configure Apt proxy — `syskit_apt_proxy`.

| Platform | Name | Value | Description |
|----------|------|-------|-------------|
| DU | `syskit_apt_proxy` | _default_ `None` | Dict {'http': {'hostname', ['directs']}, 'https': {'hostname', ['directs ']}} |

### Log Management

- Forwarding: [Rsyslog](http://www.rsyslog.com) — `syskit_logforward`
- Rotation: [Logrotate](http://www.linuxcommand.org/man_pages/logrotate8.html) — `syskit_logrotate_*`

| Platform | Name | Value | Description |
|----------|------|-------|-------------|
| DU | `syskit_logforward` | _default_ `{}` | Dict {'tcp': {'address', ['port': 514]}, 'udp': {'address', ['port': 514]}} |
| DU | `syskit_logrotate_autopurge` | _default_ `False` | Boolean. Purge logrotate if no module is defined |
| DU | `syskit_logrotate_modules` | _default_ `[]` | List of dict {'name', 'path', 'size', 'state': present/absent, 'rotate'} |

### Firewalling

Create/delete/update rules.

[Ferm](http://ferm.foo-projects.org) — `syskit_ferm_rules`

| Platform | Name | Value | Description |
|----------|------|-------|-------------|
| D | `syskit_ferm_rules` | _default_ `[]` | List of dict {'name', ['daddr'], ['proto'], ['dport'], 'state': present/absent} |

### Reverse Proxying

Ccreate/delete/update vhosts.

[Nginx](http://nginx.org/en/)

| Platform | Name | Value | Description |
|----------|------|-------|-------------|
| DU | `syskit_nginx_autopurge` | _default_ `True` | Boolean. Purge nginx if no site is defined |
| DU |`syskit_nginx_sites` | _default_ `[]` | List of dict {'name', 'state': present/absent, 'enabled': yes/no, 'upstreams', 'servers'}. An **upstream** is a dict {'name', 'servers'}. A **server** is a dict {'name', 'port', ['default'], 'tls': [{'crtval', 'keyval'}], 'locations'}. An **upstream.server** is a dict {'address', 'port', ['weight'], ['max_fails'], ['fail_timeout'], ['backup'], ['down'], ['max_conns'], ['resolve'], ['route'], ['slow_start']}. A **location** is a dict {['uri'=/], ('root', ['autoindex'=off], ['expires']) or ('proxy_pass', ['client_max_body_size'])} |
