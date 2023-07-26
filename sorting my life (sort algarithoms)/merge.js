

let merge_sort = (arr) => {
    if (arr.length === 1) {
        return arr;
    }
    let middle = Math.floor(arr.length / 2);
    let left = arr.slice(0, middle);
    let right = arr.slice(middle);
    return merge(merge_sort(left), merge_sort(right));
}

let merge = (left, right) => {
    let result = [];
    let index_left = 0;
    let index_right = 0;
    while (index_left < left.length && index_right < right.length) {
        if (left[index_left] < right[index_right]) {
            result.push(left[index_left]);
            index_left++;
        }
        else {
            result.push(right[index_right]);
            index_right++;
        }
    }
    return result.concat(left.slice(index_left)).concat(right.slice(index_right));
}

let arr = [5, 4, 3, 2, 1];
console.log(merge_sort(arr));
