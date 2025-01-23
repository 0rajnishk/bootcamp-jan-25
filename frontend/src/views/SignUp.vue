<template>
  <div>
    <h2>Sign Up</h2>
    <form @submit.prevent="signup">
      <div>
        <label for="username">Username</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div>
        <label for="email">Email</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div>
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Sign Up</button>
    </form>
  </div>


  <div>
    <p>
      <RouterLink to="/login">login</RouterLink>
    </p>
    <p>
      <RouterLink to="/">home</RouterLink>
    </p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      email: '',
      password: ''
    };
  },
  methods: {
    async signup() {
      const data = {
        username: this.username,
        email: this.email,
        password: this.password
      };

      try {
        const response = await axios.post('http://localhost:5000/signup', data);
        alert(response.data.message);
      } catch (error) {
        alert('Error during signup!');
      }
    }
  }
};
</script>
