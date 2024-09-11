var data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55];

function binary_search(arr, key) {
    let start = 0;
    let end = arr.length - 1;
    while (start <= end) {
        var mid = Math.floor((start + end) / 2);
        if (arr[mid] == key) {
            return mid;
        }
        if (arr[mid] > key) {
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }
    return -1;
}

console.log(binary_search(data, 3)); 