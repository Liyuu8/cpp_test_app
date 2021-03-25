#include <gtest/gtest.h>

#include "src/gtest/example.cpp"

TEST(example_test, func_sum)
{
  ASSERT_EQ(3, sum(1, 2));
}