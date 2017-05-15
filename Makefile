none: help

help:
	@echo "dicebox: Roll dice, flip coins, and simulate other decision-making methods."
	@echo
	@echo "run            Run dicebox directly from this repository."
	@echo "lint           Run pylint3 on the dicebox package."
	@echo "test           Run pytests for dicebox."

lint:
	@pylint3 --rcfile=pylintrc dicebox

run:
	@python3 -m dicebox

test:
	@python3 -m pytest dicebox

.PHONY: lint run test
