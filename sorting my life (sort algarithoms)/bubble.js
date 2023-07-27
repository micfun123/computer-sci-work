

let bubble = (arr) => {
    let swapped = 0;
    let temp = 0;
    for (let i = 0; i < arr.length; i++) {
        swapped = 0;
        for (let j = 0; j < arr.length - i; j++) {
            if (arr[j] > arr[j+1]) {
                temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
                swapped = 1;
            }
        }
        if (swapped === 0) {
            break;
        }
    }
    return arr;
}

let arr = [5, 4, 3, 2, 1];
console.log(bubble(arr));
