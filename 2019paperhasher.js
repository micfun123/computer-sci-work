let site = "www.ocr.org.uk";

let hash = (str) => {
    str = str.toUpperCase();
    str = str.split(".")[1];
    str = str.split(".")[0];
    //loop through string and add up the ascii values
    let total = 0;
    for (let i = 0; i < str.length; i++) {
        total += str.charCodeAt(i);
    }
    return total;
}

console.log(hash(site));