run:
	docker-compose build
	docker-compose up -d
stop:
	docker-compose down
start:
	docker-compose run tor python tor_test.py
test:
	docker-compose run tor python -m unittest discover -v
format:
	docker-compose run tor autopep8 -ivr .