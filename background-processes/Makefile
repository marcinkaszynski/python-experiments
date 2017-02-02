VENV=./venv
PYTHON=./venv/bin/python

all:
	@echo "Targets:"
	@echo " virtualenv: prepare the dev environment"
	@echo " test:       run tests"


virtualenv: $(VENV)/stamp

$(VENV)/stamp: requirements.txt
	[ -f $(PYTHON) ] || virtualenv -p python3 venv
	$(VENV)/bin/pip3 install -r requirements.txt
	touch $(VENV)/stamp

test: virtualenv
	PYTHONPATH=`pwd` $(PYTHON) background/tests.py
