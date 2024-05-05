
let data = [1,5,2,5,323,1,54,23,456]

function Linear_look(val,arr){
    for (let index = 0; index < arr.length; index++) {
        if (arr[index] == val) {
            return index
        }
    }
    return -1
}

console.log(Linear_look(2,data))
console.log(Linear_look(900,data))