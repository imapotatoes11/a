// const url = 'https://api.deepai.org/api/text-generator';
// const headers = {'Content-Type': 'application/json', 'api-key':"3d990375-0332-4da8-9092-56893149437c"};
// const body = {"text": "Say this is a test"};
// fetch(url, {method: 'POST', headers: headers, body: JSON.stringify(body),})
//     .then((response) => response.json())
//     .then((data) => {console.log(data);
// // document.getElementById('result').innerHTML=data;
// console.log(data)})
// //key 3 d 9 9 0 3 7 5 - 0 3 3 2 - 4 d a 8 - 9 0 9 2 - 5 6 8 9 3 1 4 9 4 3 7 c
///////////////////////
// const apiKey = '3d990375-0332-4da8-9092-56893149437c';
// const url = 'say this is a test';
//
// fetch('https://api.deepai.org/api/text-generator', {
//     method: 'POST',
//     headers: {
//         'api-key': apiKey,
//     },
//     body: new FormData().append('text', url),
// })
//     .then(response => response.json())
//     .then(data => {
//         console.log(data);
//     })
//     .catch(error => {
//         console.log(error)
//     });


/*
curl \
    -F 'text=YOUR_TEXT_URL' \
    -H 'api-key:3d990375-0332-4da8-9092-56893149437c' \
    https://api.deepai.org/api/text-generator
 */
//it should work but it doesn't

// Example directly sending a text string:

const deepai = require('deepai'); // OR include deepai.min.js as a script tag in your HTML

deepai.setApiKey('3d990375-0332-4da8-9092-56893149437c');

(async function() {
    var resp = await deepai.callStandardApi("text-generator", {
        text: "YOUR_TEXT_HERE",
    });
    console.log(resp);
})()