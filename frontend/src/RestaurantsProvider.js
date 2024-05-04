import axios from 'axios'
const baseUrl = 'http://localhost:5000'


const getAllGustos = () => {
	const request = axios.get(`${baseUrl}/getAllGustos`)
	return request.then(response => response.data)
}

const getSchedule = (city, depDate, retDate) => {
    const request = axios.get(`${baseUrl}/getSchedule?city=${city}&depDate=${depDate}&retDate=${retDate}`);
    return request.then(response => response.data); // Outputs the JSON response from the server)
}

export default {getAllGustos, getSchedule}