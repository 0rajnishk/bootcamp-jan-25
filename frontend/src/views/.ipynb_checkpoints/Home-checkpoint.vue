<template>
  <div class="home">
    <h1>Bootcamp App Dev</h1>
    <div>
      <p>
        <RouterLink to="/login">Login</RouterLink>
      </p>
      <p>
        <RouterLink to="/signup">Sign Up</RouterLink>
      </p>
    </div>
  </div>

  <form @submit.prevent="addTask" v-if="isLoggedin">
    <div>
      <!-- title -->
      <label for="title">Title</label>
      <input type="text" id="title" v-model="title" required />
    </div>

    <div>
      <!-- description -->
      <label for="description">Description</label>
      <textarea id="description" v-model="description" required></textarea>
    </div>

    <div>
      <!-- status -->
      <label for="status">Status</label>
      <select id="status" v-model="status">
        <option value="assigned">Assigned</option>
        <option value="in_progress">In Progress</option>
        <option value="completed">Completed</option>
      </select>
    </div>

    <!-- <div>
      <label for="assigned_to">Assigned To</label>
      <input type="text" id="assigned_to" v-model="assigned_to" required />
    </div> -->
    <!-- for assigned_to select from users -->
     <label for="assigned_to">Assigned To</label>
      <select id="assigned_to" v-model="assigned_to">
        <option v-for="user in users" :key="user.id" :value="user.id">{{ user.username }}</option>
      </select>


    <div>
      <!-- due_date -->
      <label for="due_date">Due Date</label>
      <input type="date" id="due_date" v-model="due_date" />
    </div>

    <button type="submit">Submit</button>
  </form>

    <button @click="getTodo()"> todo </button>

    <div v-if="todos!=null">
    <h2> todos </h2>
    <li v-for="(item) in todos">
      {{ item }} 
    </li>
    </div>

</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      todos: null,
      title: '',
      description: '',
      status: 'assigned',
      assigned_to: '',
      created_by: '',
      due_date: null,
      users: [],
      currentUserId: 'current_user_id', 
      isLoggedin: true, 

    };
  },

  mounted() {
    //this.getTodo();
    alert("on mount");
  },

  computed: {
    isLoggedin() {
      const access_token = localStorage.getItem('access_token');
      return access_token != null;
    }
  },

  methods: {
    async addTask(){
      const data = {
        title: this.title,
        description: this.description,
        status: this.status,
        assigned_to: this.assigned_to,
        created_by: this.created_by,
        due_date: this.due_date
      };
      const access_token = localStorage.getItem('access_token');
      if (!access_token) {
        alert('Access token is missing');
        return;
      }

      try {
        const response = await axios.post('http://localhost:5000/tasks', data, {
          headers: {
            'Authorization': `Bearer ${access_token}`
          }
        });
        alert(response.data.message);
        this.getTodo();
      } catch (error) {
        console.error(error.response || error);  // More detailed error output
        alert('Something went wrong');
      }

    },


    async getTodo() {
      const access_token = localStorage.getItem('access_token');

      if (!access_token) {
        alert('Access token is missing');
        return;
      }

      try {
        //const response = await axios.get('http://localhost:5000/todo', {

        const response = await axios.get('http://localhost:5000/todo', {
          headers: {
            'Authorization': `Bearer ${access_token}`
          }
        });
        alert(response.data.message);
        this.todos = response.data.data;
        
      } catch (error) {
        alert('Something went wrong');
      }
    },

    async fetchUsers(){
      const access_token = localStorage.getItem('access_token');
      if (!access_token) {
        alert('Access token is missing');
        return;
      }
      try {
        const response = await axios.get('http://localhost:5000/users', {
          headers: {
            'Authorization': `Bearer ${access_token}`
          }
        });
        alert(response.data.message);
        this.users = response.data.users.map(user => ({
          id: user.id,
          username: user.username,
          email: user.email,
          role: user.role
        }));
      } catch (error) {
        alert('Something went wrong');
      }
    },


    checkLogin() {
      if (!this.isLoggedin) {
        alert('You need to login first');
        this.$router.push('/login');
      }
    }


  },

  created() {
    alert('on create');
  //  this.checkLogin();
   // this.fetchUsers();
  }

};
</script>


<style scoped>
.home {
    text-align: center;
    margin-top: 50px;
}

h1 {
    font-size: 2rem;
    margin-bottom: 20px;
}

p {
    margin: 10px 0;
}

a {
    text-decoration: none;
    color: #42b983;
    font-weight: bold;
}
</style>
