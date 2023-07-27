let testdata = [5, 2, 43, 6, 1, 3, 7, 8, 9, 10, 11,21, 123, 76, 123, 4, 21]

let Bongo_Sort = (arr) => {
    while(!sorted(arr)){
        let i = Math.floor(Math.random() * arr.length)
        let j = Math.floor(Math.random() * arr.length)
        let temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        console.log(arr)
    }
    return arr
}

    

let sorted = (arr) => {
    for(let i = 0; i < arr.length - 1; i++){
        if(arr[i] > arr[i + 1]){
            return false
        }
    }
    return true
}

console.log(Bongo_Sort(testdata))
