clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -rf *.log

migra:
	. venv/bin/activate
	cd ./backend && python manage.py makemigrations && python manage.py migrate

runserver:
	. venv/bin/activate
	python backend/manage.py runserver


e2e_test:
	. venv/bin/activate
	cd ./backend && pytest -s tests/e2e/

underlords_test:
	. venv/bin/activate
	cd ./backend && pytest -s tests/underlords/