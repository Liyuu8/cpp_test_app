#include "calculate.cpp"

class BP
{
public:
  static int test(int n);
};

int BP::test(int n)
{
  bool ret = Calculate::isEven(n);
  if (ret)
    Calculate::add(n, n + 1);
}
