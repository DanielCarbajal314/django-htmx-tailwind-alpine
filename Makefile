setup:
	python3 -m venv .venv
	source ./.venv/bin/activate
	pip install -e .

up:
	docker compose up -d
	python manage.py runserver

down:
	docker compose down

make-migration:
	python manage.py makemigrations

migrate:
	python manage.py migrate