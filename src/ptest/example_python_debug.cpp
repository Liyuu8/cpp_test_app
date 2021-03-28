#include <stdio.h>

int add(int a, int b);
bool isOdd(int a);

struct Pair
{
  int l;
  int r;
};

main(void)
{
  return (0);
}

int add(int a, int b)
{
  return a + b;
}

bool isOdd(int a)
{
  return a % 2 == 1;
}

struct Pair make_pair(int l, int r)
{
  struct Pair p;
  p.l = l;
  p.r = r;
  return p;
}