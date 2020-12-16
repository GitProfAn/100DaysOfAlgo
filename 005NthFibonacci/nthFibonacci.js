// Solution 1 - recursion
// O(2^n) time / O(n) space

const getNthFib1 = (n) => {
  if (n === 2) {
    return 1;
  } else if (n === 1) {
    return 0;
  } else {
    return getNthFib1(n - 1) + getNthFib1(n - 2);
  }
};
// Solution 2 - memoization
// O(n) time / O(n) space

const getNthFib2 = (n, memoize = { 1: 0, 2: 1 }) => {
  if (n in memoize) {
    return memoize[n];
  } else {
    memoize[n] = getNthFib2(n - 1, memoize) + getNthFib2(n - 2, memoize);
    return memoize[n];
  }
};
// Solution 3 - iteration
// O(n) time / O(1) space

const getNthFib3 = (n) => {
  const lastTwo = [0, 1];
  let counter = 3;
  while (counter <= n) {
    const nextFib = lastTwo[0] + lastTwo[1];
    lastTwo[0] = lastTwo[1];
    lastTwo[1] = nextFib;
    counter++;
  }
  return n > 1 ? lastTwo[1] : lastTwo[0];
};
