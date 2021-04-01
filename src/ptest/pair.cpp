struct Pair
{
  int l;
  int r;
};

struct Pair makePair(int l, int r)
{
  struct Pair p;
  p.l = l;
  p.r = r;
  return p;
}
