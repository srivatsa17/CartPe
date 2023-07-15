import axios from "axios";

const publicAxiosInstance = axios.create({
    baseURL: 'http://localhost:8000/api/v1/',
    headers: {
        'Content-Type':'application/json'
    }
})

export default publicAxiosInstance