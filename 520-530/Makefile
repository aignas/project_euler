CC=g++
CFLAGS=-O3 -fopenmp -std=c++11 -Wall -Werror
INCLUDES=-I$(HOME)/src/test_frameworks/c++/Catch/single_include
PROBLEM=521.cxx

CFLAGS+=$(INCLUDES)

solution: $(PROBLEM)
	$(CC) $(CFLAGS) $< -o solution

all: solution

.PHONY: clean

clean:
	rm solution
