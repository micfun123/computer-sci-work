

function tohex(num)
{
    var hex = [];
    while(num > 0)
    {
        if (num % 16 > 9)
        {
            hex.append(String.fromCharCode(55 + num % 16));
        }
        else
        {
            hex.append(num % 16);
        }
        num = Math.floor(num / 16);
    }
    return hex.reverse().join("");
    }