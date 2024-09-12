
var data = [1,4,8,3,1,4,123,2];

List insertionsort(arr){
  for (var index = 0; index < arr.length; index++) {
    var key = arr[index];
    var backindex = index - 1;
    while (backindex >= 0 && key < arr[backindex]) {
      arr[backindex + 1] = arr[backindex];
      backindex = backindex -1;
    }
   }
return arr;
}

void main(){
  print(insertionsort(data));
}