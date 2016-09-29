
.PHONY: check

check:
	cd check; ansible-playbook playbook.yml
