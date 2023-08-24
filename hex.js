

function tohex(num)
{
    var hex = [];
    while(num > 0)
    {
        if (num % 16 > 9)
        {
            hex.push(String.fromCharCode(55 + num % 16));
        }
        else
        {
            hex.push(num % 16);
        }
        num = Math.floor(num / 16);
    }
    return hex.reverse().join("");
}
console.log(tohex(20));