


var data = [1,4,8,3,1,4,123,2];

List bubblesort(arr){
  var switched = true;
  while (switched) {
    switched = false;
    for (var i = 0; i < arr.length -1; i++) {
      if (arr[i] > arr[i+1]) {
        var temp = arr[i];
        arr[i] = arr[i+1];
        arr[i+1] = temp;
        switched = true;
      }
    }
    
  }
  return(arr);
}


void main(){
  print(bubblesort(data));

}
