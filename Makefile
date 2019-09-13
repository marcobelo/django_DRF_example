clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -rf *.log

populate_db:
	. venv/bin/activate
	cd ./backend/underlords/data && python populate.py

migra:
	. venv/bin/activate
	cd ./backend && python manage.py makemigrations && python manage.py migrate
	make populate_db

runserver:
	. venv/bin/activate
	python backend/manage.py runserver

underlords_test:
	. venv/bin/activate
	cd ./backend && pytest -s tests/underlords/