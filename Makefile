github_init:
	eval "$(ssh-agent -s)"
	ssh-add ~/.aaron/CCSPP/.keys/id_rsa
