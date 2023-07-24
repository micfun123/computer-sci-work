
let fizzbuzz = (int) => {
    let result = [];
    let str = "";
    for (let i = 1; i <= int; i++) {
        if (i % 3 === 0) {
            str += "Fizz";
        }
        if (i % 5 === 0) {
            str += "Buzz";
        }
        if (str === "") {
            str += i;
        }
        result.push(str);
        str = "";
    }
    return result;
    }

console.log(fizzbuzz(15));
