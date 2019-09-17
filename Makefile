clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -rf *.log

populate_db:
	. venv/bin/activate
	cd ./backend/underlords/data && python populate.py

db_create_fixture:
	. venv/bin/activate
	cd ./backend && python manage.py dumpdata --indent 4 > underlords/fixtures/db_fixture.json

migra:
	. venv/bin/activate
	cd ./backend && python manage.py makemigrations && python manage.py migrate

runserver:
	. venv/bin/activate
	python backend/manage.py runserver

underlords_test:
	. venv/bin/activate
	cd ./backend && pytest -s tests/underlords/

purge_migrations_and_database:
	cd ./backend
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc" -delete
	find . -path "*/db.sqlite3" -delete