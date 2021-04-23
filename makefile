.PHONY: test build

build:
	docker build --no-cache --force-rm -t stockbot .

run:
	docker run --rm -i -t stockbot

test:
	python -m unittest discover -s tests -p 'test_*.py'

rstdoc:
	sphinx-apidoc -o docs/source/ stockbot/

doc:
	make -C docs html