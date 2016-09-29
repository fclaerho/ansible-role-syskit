
**Syskit** is an [Ansible role](https://docs.ansible.com/playbooks_roles.html) designed to ease the integration of platform independent services and tools on specific platforms. It handles the configuration of system specific concerns such as users, service manifests, logging management and various networking aspects.

You can use this role from a **playbook**,
by adding its ID to the `requirements.yml/txt` file
and then calling `ansible-galaxy install -r requirements.yml/txt`,
or you can use it as another **role dependency**,
by adding its ID in the `dependencies` list of the role manifest `meta/main.yml`.
The **stable version** of this role is registered on Galaxy with the ID `fclaerho.syskit`;
you can alternatively use this repository URL as ID for the **development version**.

The following **platforms** are currently supported: Debian (D), Ubuntu (U) and macOS ().

NOTICE! All private keys `*.keyval` should be securely stored via [Ansible-vault](http://docs.ansible.com/ansible/playbooks_vault.html) (or any equivalent.)


#### USERS

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
| – | `syskit_users` | `[]` | List of dict `{'name', ['home'], ['shell': /bin/bash], 'state': present/absent, ['groups'], 'sudoer': yes/no, 'sshkeys': {'name', 'keyval', 'pubval', 'state': present/absent}…, 'authorized_keys': {'val', 'state': present/absent}…}` |
| DU | `syskit_root_pw_locked` | `false` | Boolean. If set, lock root password (recommended) |


#### SERVICE MANIFESTS

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
| D | `syskit_sysv_manifests` | `[]` | List of dict `{'uid', 'name', 'argv', 'state': present/absent, 'daemon', ['pidfile'], 'description'}` |
| U | `syskit_upstart_manifests` | `[]` | List of dict `{'uid', 'name', 'argv', 'state': present/absent, 'daemon', 'description'}` |

Tools:
[Upstart](http://upstart.ubuntu.com/cookbook/) |
[SysV](https://en.wikipedia.org/wiki/Init#SysV-style)


#### APPLICATIONS

NOTICE! On macOS, setting an application as `absent` will purge its configuration and any related package or container. Make sure to have a backup of your application defaults.

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
|  | `syskit_macosx_apps` | [] | List of dict `{'name', 'state': present/absent, 'domains', 'defaults': path}` |


#### PACKAGE MANAGEMENT

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
| DU | `syskit_apt_proxy` | `None` | Dict `{'http': {'hostname', ['directs']}, 'https': {'hostname', ['directs ']}}` |


#### LOGGING MANAGEMENT

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
| DU | `syskit_logforward` | `{}` | Dict `{'tcp': {'address', ['port': 514]}, 'udp': {'address', ['port': 514]}}` |
| DU | `syskit_logrotate_autopurge` | `False` | Boolean. Purge logrotate if no module is defined |
| DU | `syskit_logrotate_modules` | `[]` | List of dict `{'name', 'path', 'size', 'state': present/absent, 'rotate'}` |

Tools:
[Rsyslog](http://www.rsyslog.com) |
[Logrotate](http://www.linuxcommand.org/man_pages/logrotate8.html)


#### FIREWALLING

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
| D | `syskit_ferm_rules` | `[]` | List of dict `{'name', ['daddr'], ['proto'], ['dport'], 'state': present/absent}` |

Tools:
[Ferm](http://ferm.foo-projects.org)


#### REVERSE PROXYING

| Platform | Name | Default | Description |
|----------|------|---------|-------------|
| DU | `syskit_nginx_autopurge` | `True` | Boolean. Purge nginx if no site is defined |
| DU |`syskit_nginx_sites` | `[]` | List of dict `{'name', 'state': present/absent, 'enabled': yes/no, 'upstreams', 'servers'}`. An **upstream** is a dict `{'name', 'servers'}`. A **server** is a dict `{'name', 'port', ['default'], 'tls': [{'crtval', 'keyval'}], 'locations'}`. An **upstream.server** is a dict `{'address', 'port', ['weight'], ['max_fails'], ['fail_timeout'], ['backup'], ['down'], ['max_conns'], ['resolve'], ['route'], ['slow_start']}. A **location** is a dict {['uri'=/], ('root', ['autoindex'=off], ['expires']) or ('proxy_pass', ['client_max_body_size'])}` |

Tools:
[Nginx](http://nginx.org/en/)
