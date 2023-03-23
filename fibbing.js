
var a = 0;
var b = 1;
//set the end of the sequence via user input
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});
  
readline.question(`What's the amount of times to go throught?`, end => {
    //turn end in to a int
    end = parseInt(end);
    
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

    readline.close();
});
