// https://codingbat.com/prob/p154669

public int factorial(int n) {
  if (n == 0) {
    return 1;
  }
  return n * factorial(n-1);
}

