
**Syskit** (System Integration Kit) helps you integrates your services and tools by configuring system specific concerns such as users, service management, logging and various networking aspects.

The stable version of this roleis registered on Galaxy with the ID `fclaerho.syskit`;
you can alternatively use this repository URL as ID (development version.)
You can use this role from a **playbook**,
by adding its ID to the project `requirements.{txt,yml}` file,
or you can use it as another **role dependency**,
by adding its ID in the `dependencies` list of the role manifest `meta/main.yml`.
For further **usage** details,
please refer to the Ansible documentation at https://docs.ansible.com/playbooks_roles.html.

All private keys `*.keyval` should be securely stored via [Ansible-vault](http://docs.ansible.com/ansible/playbooks_vault.html) (or any equivalent.)

**Supported platforms** at the moment: Debian (D), Ubuntu (U) and macOS ().

### CONCERNS

#### USERS

Create/delete/update accounts.

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
| – | `syskit_users` | `[]` | List of dict `{'name', ['home'], ['shell': /bin/bash], 'state': present/absent, ['groups'], 'sudoer': yes/no, 'sshkeys': {'name', 'keyval', 'pubval', 'state': present/absent}…, 'authorized_keys': {'val', 'state': present/absent}…}` |
| DU | `syskit_root_pw_locked` | `false` | Boolean. If set, lock root password (recommended) |


#### SERVICES

Create/delete/update service manifests.

Supported service managers:

- [Upstart](http://upstart.ubuntu.com/cookbook/)
- [SysV](https://en.wikipedia.org/wiki/Init#SysV-style)

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
| D | `syskit_sysv_manifests` | `[]` | List of dict `{'uid', 'name', 'argv', 'state': present/absent, 'daemon', ['pidfile'], 'description'}` |
| U | `syskit_upstart_manifests` | `[]` | List of dict `{'uid', 'name', 'argv', 'state': present/absent, 'daemon', 'description'}` |


#### APPLICATIONS

Install/purge applications.

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
|  | `syskit_macosx_apps` | [] | List of dict `{'name', 'state': present/absent, 'domains', 'defaults': path}` |


#### PACKAGE MANAGEMENT

Supported package managers:

- apt

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
| DU | `syskit_apt_proxy` | `None` | Dict `{'http': {'hostname', ['directs']}, 'https': {'hostname', ['directs ']}}` |


#### LOG MANAGEMENT

- [Rsyslog](http://www.rsyslog.com)
- [Logrotate](http://www.linuxcommand.org/man_pages/logrotate8.html)

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
| DU | `syskit_logforward` | `{}` | Dict `{'tcp': {'address', ['port': 514]}, 'udp': {'address', ['port': 514]}}` |
| DU | `syskit_logrotate_autopurge` | `False` | Boolean. Purge logrotate if no module is defined |
| DU | `syskit_logrotate_modules` | `[]` | List of dict `{'name', 'path', 'size', 'state': present/absent, 'rotate'}` |


#### FIREWALLING

Create/delete/update rules.

Supported frontends:

- [Ferm](http://ferm.foo-projects.org)

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
| D | `syskit_ferm_rules` | `[]` | List of dict `{'name', ['daddr'], ['proto'], ['dport'], 'state': present/absent}` |


#### REVERSE PROXYING

Ccreate/delete/update vhosts.

Supported servers:

- [Nginx](http://nginx.org/en/)

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
| DU | `syskit_nginx_autopurge` | `True` | Boolean. Purge nginx if no site is defined |
| DU |`syskit_nginx_sites` | `[]` | List of dict `{'name', 'state': present/absent, 'enabled': yes/no, 'upstreams', 'servers'}. An **upstream** is a dict {'name', 'servers'}. A **server** is a dict {'name', 'port', ['default'], 'tls': [{'crtval', 'keyval'}], 'locations'}. An **upstream.server** is a dict {'address', 'port', ['weight'], ['max_fails'], ['fail_timeout'], ['backup'], ['down'], ['max_conns'], ['resolve'], ['route'], ['slow_start']}. A **location** is a dict {['uri'=/], ('root', ['autoindex'=off], ['expires']) or ('proxy_pass', ['client_max_body_size'])}` |


#### MAINTENANCE

To check the role usability, in `check/`, run:

	$ ansible-playbook playbook.yml
