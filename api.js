// simple API demo 

const axios = require('axios');

// url
let url = "https://data.binance.com/api/v3/ticker/24hr"

// get data and print the price of the first item
axios.get(url)
    .then((response) => {
        // handle success
        console.log(response.data[0].lastPrice);
    }
    )
    




