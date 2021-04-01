class Calculate
{
public:
  static int add(int a, int b);
  static bool isOdd(int a);
  static bool isEven(int a);
};

int Calculate::add(int a, int b)
{
  return a + b;
}

bool Calculate::isOdd(int n)
{
  return n % 2 == 1;
}

bool Calculate::isEven(int n)
{
  return n % 2 == 0;
}