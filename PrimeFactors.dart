

List<int> divisors(int integer) {
  List<int> factors = [];
  for (int i = 2; i <= integer ~/ 2; i++) {
    if (integer % i == 0) {
      factors.add(i);
      if (i != integer ~/ i) {
        factors.add(integer ~/ i);
      }
    }
  }
  if (factors.isEmpty) {
    return [integer]; 
  }
  return factors;
}

void main() {
  print(divisors(12)); // Output: [2, 3, 4, 6]
  print(divisors(25)); // Output: [5]
  print(divisors(13)); // Output: [13] (since 13 is prime)
}
