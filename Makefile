deploy:
	git push heroku `git subtree split --prefix server master`:master --force

test:
	pytest server

install-deps:
	pip install -r server/requirements.txt
