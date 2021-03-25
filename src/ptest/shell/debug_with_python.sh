#!/bin/sh

gcc -g3 src/ptest/example_python_debug.cpp && \
gdb -q -x src/ptest/test/debug.py a.out
