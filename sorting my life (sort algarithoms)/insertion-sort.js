
let Insertion_Sort = (arr) => {
    for (let i = 0; i < arr.length; i++){
        let key = arr[i]
        let j = i -1
        while( j >= 0 && arr[j] > key){
            arr[j + 1] = arr[j]
            j = j - 1
        }
        arr[j + 1] = key
        
    }
    return arr
}

let testdata = [5, 2, 4, 6, 1, 3]
console.log(Insertion_Sort(testdata))