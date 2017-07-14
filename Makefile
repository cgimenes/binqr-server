deploy:
	git push heroku master

test:
	pytest

install-deps:
	pip install -r requirements.txt
