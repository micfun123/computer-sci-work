let tocode = "cccaab"

//run length encoding string
let encode = (str) => {
    let result = ""
    let count = 1
    for (let i = 0; i < str.length; i++) {
        if (str[i] === str[i + 1]) count++
        else {
            result += count + str[i]
            count = 1
        }
    }
    return result
}

//run length decoding string
let decode = (str) => {
    let result = ""
    let count = ""
    for (let i = 0; i < str.length; i++) {
        if (isNaN(str[i])) {
            result += str[i].repeat(count)
            count = ""
        } else count += str[i]
    }
    return result
}

console.log(encode(tocode))
console.log(decode(encode(tocode)))

