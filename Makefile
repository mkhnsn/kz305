# Thin wrapper so `make` works as muscle memory. All configuration lives in
# harness.yml; ./render is the real entry point.
.PHONY: all list clean
all:
	./render
list:
	./render --list
clean:
	rm -rf out
