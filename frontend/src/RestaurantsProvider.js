import axios from 'axios'
const baseUrl = 'http://localhost:5000'


const getAllGustos = () => {
	const request = axios.get(`${baseUrl}/getAllGustos`)
	return request.then(response => response.data)
}

function fetchData() {
    axios.get('http://localhost:5000/getPlan')
        .then(response => {
            console.log(response.data); // Outputs the JSON response from the server
        })
        .catch(error => {
            console.error('Error:', error); // Outputs errors to the console
        });
}

export default {getAllGustos}

