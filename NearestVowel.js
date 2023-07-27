let Vowels = ['a', 'e', 'i', 'o', 'u']

function nearestVowel (letter) {
    let index = Vowels.indexOf(letter)
    //if letter is in the array, return it
    if (index !== -1) {
        return Vowels[index]
    }
    //if letter is not in the array, find the nearest vowel
    else {
        while (index === -1) {
            letter = String.fromCharCode(letter.charCodeAt(0) + 1)
            index = Vowels.indexOf(letter)
        }
        return Vowels[index]
    }
}

console.log(nearestVowel('c'))
console.log(nearestVowel('e'))
console.log(nearestVowel('y'))