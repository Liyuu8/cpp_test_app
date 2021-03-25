#!/bin/sh

g++ -std=c++11 src/gtest/test/example_mock_test.cpp -I. -Isrc \
  -Igoogletest/googletest-release-1.10.0/googletest/include \
  -Igoogletest/googletest-release-1.10.0/googlemock/include \
  -Lgoogletest -lgtest -lgtest_main -lgmock -lgmock_main -lpthread && \

./a.out
