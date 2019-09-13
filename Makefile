clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -rf *.log

runserver:
	. venv/bin/activate
	python backend/manage.py runserver

migra:
	. venv/bin/activate
	cd ./backend && python manage.py makemigrations && python manage.py migrate

e2e_test:
	. venv/bin/activate
	make migra
	cd ./backend && pytest -s