<template>
    <div>
        <h2>Login</h2>
        <form @submit.prevent="login">
            <div>
                <label for="email">Email</label>
                <input type="email" id="email" v-model="email" required />
            </div>
            <div>
                <label for="password">Password</label>
                <input type="password" id="password" v-model="password" required />
            </div>
            <button type="submit">Login</button>
        </form>
    </div>

    <div>
        <p>
            <RouterLink to="/">home</RouterLink>
        </p>
        <p>
            <RouterLink to="/signup">Sign Up</RouterLink>
        </p>
    </div>
    
</template>


<script>
import axios from 'axios';

export default {
    data() {
        return {
            email: '',
            password: ''
        };
    },
    methods: {
        // async login() {
        //     const data = {
        //         email: this.email,
        //         password: this.password
        //     };

        //     try {
        //         const response = await axios.post('http://localhost:5000/login', data);
        //         alert(response.data.message);
        //         // set access_token to the local storage 
        //         localStorage.setItem('access_token', response.data.access_token);

        //     } catch (error) {
        //         alert('Login failed!');
        //     }
        // }
        async login() {
            const data = {
                email: this.email,
                password: this.password
            };


            try {
                const response = await fetch('http://localhost:5000/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });
        
                if (!response.ok) {
                    throw new Error('Login failed!');
                }
        
                const responseData = await response.json();
                alert(responseData.message);
        
                // Set access_token to local storage
                localStorage.setItem('access_token', responseData.access_token);
                this.$router.push('/');
            } catch (error) {
                alert(error.message || 'Login failed!');
            }
        } // login


    }
};
</script>


