let babys =  ["anna", "bob", "charlie","Michael"]
let weights = [7.5, 8.2, 9.1, 7.7]

function babyWeightMean (babys, weights) {
    let average = 0
    for (let i = 0; i < babys.length; i++) {
        average += weights[i]
    }
    average = average / babys.length
    console.log(average)
    let total = 0
    for (let i = 0; i < babys.length; i++) {
        if (weights[i] > average) {
            total += 1
        }
    }
    console.log(total)
}

babyWeightMean(babys, weights)

