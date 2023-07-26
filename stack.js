let stack = []
let max = 15

let add = (int) => {
    if (stack.length < max) {
        stack.push(int)
    }
    else {
        console.log("Stack overflow")
    }
}


let pop = (int) => {
    let data = stack[stack.length - 1]
    stack.pop()
    return data
}

let peek = () => {
    return stack[stack.length - 1]
}

let show = () => {
    return stack
}

for ( let i = 0; i < 5; i++) {
    add(i)
}

console.log(show())
console.log(pop())
console.log(show())
console.log(peek())
console.log(add(5))
console.log(show())
