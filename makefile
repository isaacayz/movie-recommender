# Declare variables and automations


PYTHON = python
SRC_DIR = src
VENV_DIR = venv


.PHONY: setup
setup:
	$(PYTHON) -m venv $(VENV_DIR)
	. $(VENV_DIR)/bin/activate; pip install -r requirements.txt

.PHONY: run
run:
	. $(VENV_DIR)/bin/activate; $(PYTHON) $(SRC_DIR)/app.py


.PHONY: clean
clean:
	rm -rf $(VENV_DIR)


.PHONY: all
all:
	setup run