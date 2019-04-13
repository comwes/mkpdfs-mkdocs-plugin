PROJECT_NAME := $(shell python3 setup.py --name)
PROJECT_VERSION := $(shell python3 setup.py --version)

SHELL := /bin/bash
BOLD := \033[1m
DIM := \033[2m
RESET := \033[0m

bold=$(tput bold)
reset=$(tput sgr0)
green := $(tput setaf 2)

.PHONY: dist
dist: clean build install


.PHONY: build
build:
	@tput bold && tput setaf 2
	@echo "Building package $(PROJECT_NAME) $(PROJECT_VERSION)"
	@tput sgr0
	@pip3 install npm
	@python3 design.py
	@python3 setup.py sdist bdist_wheel

.PHONY: install
install:
	@pip3 install dist/$(PROJECT_NAME)-$(PROJECT_VERSION).tar.gz

.PHONY: clean
clean:
	@tput bold && tput setaf 2
	@echo "Cleaning up ... "
	@tput sgr0
	@rm -rf dist

.PHONY: develop
develop:
	@tput bold && tput setaf 2
	@echo "Installing package for development purpose $(PROJECT_NAME) $(PROJECT_VERSION)"
	@tput sgr0
	@pip3 install npm
	@python3 design.py
	@pip3 install -e .
