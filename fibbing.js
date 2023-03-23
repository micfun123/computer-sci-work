
var a = 0;
var b = 1;
var end = 10;
var c = 0;
var total = 0;

list = [];
for (var i = 0; i < end; i++) {
    c = a + b;
    a = b;
    b = c;
    list.push(c);
    total += c;

}

console.log(list);
console.log(total);
