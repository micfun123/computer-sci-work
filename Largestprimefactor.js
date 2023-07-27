
let targer = 650
let primefactors = []
for (let i = 2; i < targer; i++) {
    if (targer % i === 0) {
        primefactors.push(i)
    }
}
console.log(primefactors)


