<template>
  <div class="register-container">
    <div class="register-form">
      <h2>Register</h2>
      <form @submit.prevent="register">
        <input v-model="username" placeholder="Username" class="input-field" />
        <input v-model="email" placeholder="Email" class="input-field" />
        <input type="password" v-model="password" placeholder="Password" class="input-field" />
        <button type="submit" class="register-button">Register</button>
      </form>
      <button @click="goToLogin" class="login-button">Zurück zum Login</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const username = ref('');
const email = ref('');
const password = ref('');
const router = useRouter();

const register = () => {
  axios.post('/api/register/', { username: username.value, email: email.value, password: password.value })
    .then(response => {
      console.log(response.data);
    })
    .catch(error => {
      console.error(error);
    });
};

const goToLogin = () => {
  router.push('/login');
};
</script>

<style scoped>
body {
  font-family: 'Arial', sans-serif;
  background-color: #f5f5f5;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}

.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

.register-form {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
  width: 300px;
}

.register-form h2 {
  margin-bottom: 1.5rem;
  color: #34B466;
}

.input-field {
  width: 100%;
  padding: 0.75rem;
  margin-bottom: 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.input-field:focus {
  border-color: #34B466;
  outline: none;
  box-shadow: 0 0 5px rgba(52, 180, 102, 0.5);
}

.register-button, .login-button {
  width: 100%;
  padding: 0.75rem;
  border: none;
  border-radius: 4px;
  background-color: #34B466;
  color: white;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.register-button:hover, .login-button:hover {
  background-color: #2d9c55;
}

.login-button {
  margin-top: 1rem;
  background-color: #fff;
  color: #34B466;
  border: 1px solid #34B466;
}

.login-button:hover {
  background-color: #f5f5f5;
}
</style>