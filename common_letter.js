let teststring = "aafbbccddaaaaadeeefff";

let common_letter = (str) => {
    lowerstr = str.toLowerCase();
    //find the most common letter in a string
    let lettercount = {};
    for (let i = 0; i < lowerstr.length; i++) {
        if (lettercount[lowerstr[i]]) {
            lettercount[lowerstr[i]]++;
        } else {
            lettercount[lowerstr[i]] = 1;
        }
    }
    let maxcount = 0;
    let maxletter = "";
    for (let letter in lettercount) {
        if (lettercount[letter] > maxcount) {
            maxcount = lettercount[letter];
            maxletter = letter;
        }
    }
    return maxletter + " appears " + maxcount + " times.";


}

console.log(common_letter(teststring));