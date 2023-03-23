
// do the fibinarchi thing
var a = 0;
var b = 1;
var c = 0;
var total = 0;

list = [];
for (var i = 0; i < 10; i++) {
    c = a + b;
    a = b;
    b = c;
    list.push(c);
    total += c;

}

console.log(list);
console.log(total);
