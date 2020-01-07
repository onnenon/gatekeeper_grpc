run: 
	python -m gatekeeper_grpc

clean:
	find . -name '*.pyc' -exec rm '{}' ';'
	find . -name '__pycache__' -type d -prune -exec rm -rf '{}' '+'
	find . -name '.pytest_cache' -type d -prune -exec rm -rf '{}' '+'

scrub: clean
	find . -name '*.egg-info' -type d -prune -exec rm -rf '{}' '+'
	rm -rf htmlcov
	rm -f .coverage

format:
	isort -rc gatekeeper tests
	black gatekeeper tests

test:
	python3 -m coverage run --source gatekeeper -m pytest tests -p no:warnings

review: format test
