const axios = require('axios');

function fetchData() {
    axios.get('http://localhost:5000/getPlan')
        .then(response => {
            console.log(response.data); // Outputs the JSON response from the server
        })
        .catch(error => {
            console.error('Error:', error); // Outputs errors to the console
        });
}

function getPreferences() {
    
}

fetchData(); // Executes the function
