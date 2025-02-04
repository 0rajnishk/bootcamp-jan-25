import { createRouter, createWebHistory } from 'vue-router'
import SignUp from '../views/SignUp.vue'
import Login from '../views/Login.vue'
import Home from '../views/Home.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/signup',
            name: 'signup',
            component: SignUp
        },
        {
            path: '/login',
            name: 'login',
            component: Login
        }

    ]
})

export default router