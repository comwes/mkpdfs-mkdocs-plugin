PROJECT_NAME := $(shell python3 setup.py --name)
PROJECT_VERSION := $(shell python3 setup.py --version)

SHELL := /bin/bash
BOLD := \033[1m
DIM := \033[2m
RESET := \033[0m

bold=$(tput bold)
reset=$(tput sgr0)
green := $(tput setaf 2)
.DEFAULT_GOAL := dist

.PHONY: dist
dist: clean build



.PHONY: build
build:
	@tput bold && tput setaf 2
	@echo "Building package $(PROJECT_NAME) $(PROJECT_VERSION)"
	@tput sgr0
	@pip3 install npm
	@python3 design.py
	@rm -rf "$(PROJECT_NAME)/design/node_modules"
	@python3 setup.py sdist

.PHONY: clean
clean:
	@tput bold && tput setaf 2
	@echo "Cleaning up ... "
	@tput sgr0
	@rm -rf dist

.PHONY: dryrun
dryrun:
	@tput bold && tput setaf 2
	@echo "Testing packaging $(PROJECT_NAME) $(PROJECT_VERSION)"
	@tput sgr0
	@pip3 install npm
	@python3 design.py
	@rm -rf "$(PROJECT_NAME)/design/node_modules"
	@python3 setup.py sdist -n
