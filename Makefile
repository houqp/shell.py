all: test

test:
	# need at least nosetests 1.3.0
	nosetests


clean:
	rm -rf build dist *.egg-info

.PHONY: all clean

