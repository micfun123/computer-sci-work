let datatosort = [3, 6, 8, 10, 1, 2, 1,42,15,57]

function stalinSort(arr) {
    let sorted = [arr[0]]
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] >= sorted[sorted.length - 1]) {
            sorted.push(arr[i])
        }
    }
    return sorted
}

console.log(stalinSort(datatosort)) // [3, 6, 8, 10, 42, 57]
