
String FizzBuzz(int n){
  var Output = "";

  if (n % 3 == 0) {
    Output = Output + "Fizz";
  }
  if (n % 5 == 0) {
    Output = Output + "Buzz";
  }
  if (Output == ""){
    Output = n.toString();
  }

  return Output;
}

void main(){
  print(FizzBuzz(5));
  print(FizzBuzz(15));
  print(FizzBuzz(25));
  print(FizzBuzz(7));
}