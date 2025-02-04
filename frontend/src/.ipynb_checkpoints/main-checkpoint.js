import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import axios from "axios";

// global Axios instance
const instance = axios.create({
    baseURL: "http://127.0.0.1:5000/",
});

const app = createApp(App)


app.use(router)

app.mount('#app')

// import { createApp } from 'vue'
// import './style.css'
// import App from './App.vue'

// createApp(App).mount('#app')
