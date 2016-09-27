
### Synopsis

Syskit — Deploy your services and tools then let syskit handle the integration by configuring system specific concerns such as users, service manifests, logging, proxying, firewalling and so on.

### Usage

This role is registered on Galaxy with the ID `fclaerho.syskit`;
You can alternatively use this repository URL as ID.

- to use this role from a **playbook**, 
  add its ID to the project `requirements.{txt,yml}` file.
- to add this role as another **role dependency**,
  add its ID in the `dependencies` list of the role manifest `meta/main.yml`.

For further details,
please refer to the Ansible documentation at https://docs.ansible.com/playbooks_roles.html.

All private keys `*.keyval` should be securely stored via [Ansible-vault](http://docs.ansible.com/ansible/playbooks_vault.html) (or any equivalent.)

### Concerns

Supported platforms:
- D: Debian
- U: Ubuntu
- : macOS
- *: Any

#### Users

Create/delete/update accounts.

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
| * | `syskit_users` | `[]` | List of dict {'name', ['home'], ['shell': /bin/bash], 'state': present/absent, ['groups'], 'sudoer': yes/no, 'sshkeys': {'name', 'keyval', 'pubval', 'state': present/absent}…, 'authorized_keys': {'val', 'state': present/absent}…} |
| DU | `syskit_root_pw_locked` | `false` | Boolean. If set, lock root password (recommended) |


#### Services

Create/delete/update service manifests.

Supported service managers:
- [Upstart](http://upstart.ubuntu.com/cookbook/)
- [SysV](https://en.wikipedia.org/wiki/Init#SysV-style)

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
| D | `syskit_sysv_manifests` | `[]` | List of dict {'uid', 'name', 'argv', 'state': present/absent, 'daemon', ['pidfile'], 'description'} |
| U | `syskit_upstart_manifests` | `[]` | List of dict {'uid', 'name', 'argv', 'state': present/absent, 'daemon', 'description'} |


#### Applications

Install/purge applications.

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
|  | `syskit_macosx_apps` | [] | List of dict {'state': present/absent, 'defaults': path} |


#### Package Management

Supported package managers:
- apt

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
| DU | `syskit_apt_proxy` | `None` | Dict {'http': {'hostname', ['directs']}, 'https': {'hostname', ['directs ']}} |


#### Log Management

- [Rsyslog](http://www.rsyslog.com)
- [Logrotate](http://www.linuxcommand.org/man_pages/logrotate8.html)

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
| DU | `syskit_logforward` | `{}` | Dict {'tcp': {'address', ['port': 514]}, 'udp': {'address', ['port': 514]}} |
| DU | `syskit_logrotate_autopurge` | `False` | Boolean. Purge logrotate if no module is defined |
| DU | `syskit_logrotate_modules` | `[]` | List of dict {'name', 'path', 'size', 'state': present/absent, 'rotate'} |


#### Firewalling

Create/delete/update rules.

Supported frontends:
- [Ferm](http://ferm.foo-projects.org)

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
| D | `syskit_ferm_rules` | `[]` | List of dict {'name', ['daddr'], ['proto'], ['dport'], 'state': present/absent} |


#### Reverse Proxying

Ccreate/delete/update vhosts.

Supported servers:
- [Nginx](http://nginx.org/en/)

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
| DU | `syskit_nginx_autopurge` | `True` | Boolean. Purge nginx if no site is defined |
| DU |`syskit_nginx_sites` | `[]` | List of dict {'name', 'state': present/absent, 'enabled': yes/no, 'upstreams', 'servers'}. An **upstream** is a dict {'name', 'servers'}. A **server** is a dict {'name', 'port', ['default'], 'tls': [{'crtval', 'keyval'}], 'locations'}. An **upstream.server** is a dict {'address', 'port', ['weight'], ['max_fails'], ['fail_timeout'], ['backup'], ['down'], ['max_conns'], ['resolve'], ['route'], ['slow_start']}. A **location** is a dict {['uri'=/], ('root', ['autoindex'=off], ['expires']) or ('proxy_pass', ['client_max_body_size'])} |
