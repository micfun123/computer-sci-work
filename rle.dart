
var testdata = "aaccttvpssss";

String rle(data){
  var compressed = "";
  var count = 1;

  for(var i = 0; i < data.length; i++){
    if (i == 0) {
      compressed = compressed + data[1];
    }
    else if(data[i] == data[i -1 ]){
      count = count + 1;
    }
    else{
      compressed = compressed + count.toString() + data[i];
      count = 1;
    }

  }
  compressed = compressed + count.toString();

  return compressed;
}

void main(){
  print(rle(testdata));
}