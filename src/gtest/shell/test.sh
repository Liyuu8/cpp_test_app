#!/bin/sh

g++ -std=c++11 src/gtest/test/example_test.cpp -I. -Isrc \
  -Igoogletest/googletest-release-1.10.0/googletest/include \
  -Lgoogletest/googletest-release-1.10.0/lib \
  -lgtest -lgtest_main -lpthread && \

./a.out
