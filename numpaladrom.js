let paladrom = (int) => {
    let str = int.toString()
    let rev = str.split('').reverse().join('')
    return str === rev
}

console.log(paladrom(12321));
console.log(paladrom(1));
console.log(paladrom(1231));

