all: test

test:
	nosetests


clean:
	rm -rf build dist *.egg-info

.PHONY: all clean

