ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

.PHONY: setup
setup:
	conda env update -f conda.yml --prune
