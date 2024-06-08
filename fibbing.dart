import 'dart:io'; // used to take a input from terminal


void main(){
  var a = 0;
  var b = 1;
  var z = 0;
  print("Enter the amount of of itterations to do: ");
  int? amount = int.parse(stdin.readLineSync()!); //takes inpute (for some reason only as a string) then parses it to a int
  for (var i = 0; i < amount; i++) {
    z = a + b;
    print(z);
    a = b;
    b = z;
  }
}