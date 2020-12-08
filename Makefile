
build: ## build
	echo build

test: ## test
	python -m pytest --disable-warnings ##test_taskheap.py 

clean: ## clean all the things
	echo implement clean makefile rule

work-emacs: ## open all files in editor
	emacs README.md *.py

# http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk \
	'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

FORCE:

