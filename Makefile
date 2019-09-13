clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -rf *.log

e2e_test:
	. venv/bin/activate
	pytest -sv tests/e2e/