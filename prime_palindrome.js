function isprime(num){
    if (num < 2) {
        return false
    }
    if (num == 2) {
        return true;
    }
    if (num % 2 == 0) {
        return false;
    }
    let max_divisor = Math.floor((num ** 0.5) + 1);
    for (let index = 3; index < max_divisor; index = index + 2) {
        if(num % index == 0){
            return false;
        }
    }
    return true
}

function is_palindrome(num){
    num = num.toString()
    if (num == num.split('').reverse().join('')) {
        return true
    }
}

let values = [];
for (let index = 0; index < 200; index++) {
    if (is_palindrome(index) && isprime(index)) {
        values.push(index);
    }
}
console.log(values);