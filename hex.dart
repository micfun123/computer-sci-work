String toHex(num n) {
  List<String> hex = [];
  while (n > 0) {
    int remainder = n.toInt() % 16;
    if (remainder > 9) {
      hex.add(String.fromCharCode(55 + remainder));
    } else {
      hex.add(remainder.toString());
    }
    n = (n / 16).floor();
  }
  hex = hex.reversed.toList();
  var out = hex.join();
  
  return out.isEmpty ? '0' : out;
}

void main() {
  print(toHex(5));   // Expected output: 5
  print(toHex(10));  // Expected output: A
  print(toHex(55));  // Expected output: 37
}
