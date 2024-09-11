var data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55];

int binary_search(arr,key){
  var start = 0;
  var end = arr.length -1;
  while (start <= end) {
    var mid = ((start + end) / 2).floor();
    if (arr[mid] == key) {
      return mid;
    }
    if(arr[mid] > key){
      end = mid -1;
    }
    else{
      start = mid +1;
    }
  }
  return -1;
}

void main(){
  print(binary_search(data, 7));
  print(binary_search(data, 70));
  print(binary_search(data, 9));
  print(binary_search(data, 99));
  print(binary_search(data, 2));
}