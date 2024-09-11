
int Linear_search(arr,key){
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] == key) {
      return i;
    }
  }
  return -1;
}


void main() { 
  var data = [1,5,2,5,323,1,54,23,456]; 
  print(Linear_search(data,2));
  print(Linear_search(data,5));
  print(Linear_search(data,9999));
}