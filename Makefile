deploy:
	git push heroku master

test:
	pytest

coverage:
	pytest --cov-branch --cov=src tests


install-deps:
	pip install -r requirements.txt
