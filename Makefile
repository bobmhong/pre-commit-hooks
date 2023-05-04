.PHONY: install
install:
	@./install-requirements.sh
	@pre-commit install
