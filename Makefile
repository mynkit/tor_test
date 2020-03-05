run:
	docker-compose build
	docker-compose up -d
stop:
	docker-compose down
start:
	docker-compose run tor python tor_test.py
