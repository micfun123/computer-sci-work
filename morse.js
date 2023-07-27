let messageout = []
let messagein = "Cats are cute"

let morselookup = {
    a: ".-",
    b: "-...",
    c: "-.-.",
    d: "-..",
    e: ".",
    f: "..-.",
    g: "--.",
    h: "....",
    i: "..",
    j: ".---",
    k: "-.-",
    l: ".-..",
    m: "--",
    n: "-.",
    o: "---",
    p: ".--.",
    q: "--.-",
    r: ".-.",
    s: "...",
    t: "-",
    u: "..-",
    v: "...-",
    w: ".--",
    x: "-..-",
    y: "-.--",
    z: "--.."

}

let morse_encoder = (message) => {
    let messagearray = message.split("")
    messagearray.forEach((letter) => {
        messageout.push(morselookup[letter])
    })
    console.log(messageout.join(" "))
}

morse_encoder(messagein)

let morse_decoder = (message) => {
    let messagearray = message.split(" ")
    messagearray.forEach((letter) => {
        messageout.push(" ")
        for (let key in morselookup) {
            if (morselookup[key] === letter) {
                messageout.push(key)
            }
            else if (letter === "") {
                messageout.push(" ")
            }
        }
    })
    console.log(messageout.join(""))
}

morse_decoder(".- - ...  .- .-. .  -.-. ..- - .")


