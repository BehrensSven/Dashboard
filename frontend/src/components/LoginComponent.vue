<template>
  <div class="login-container">
    <div class="login-form">
      <h2>Login</h2>
      <form @submit.prevent="login">
        <input v-model="username" placeholder="Username" class="input-field" />
        <input type="password" v-model="password" placeholder="Password" class="input-field" />
        <button type="submit" class="login-button">Login</button>
      </form>
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      <button @click="goToRegister" class="register-button">Registrierung</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const username = ref('');
const password = ref('');
const errorMessage = ref('');
const router = useRouter();

const login = () => {
      axios.post('http://127.0.0.1:8050/api/token/', { username: username.value, password: password.value })
        .then(response => {
          if (response.data.access) {
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);
            router.push('/dashboard');
          } else {
            console.error('No access token received');
            errorMessage.value = 'Login failed. Please try again.';
          }
        })
        .catch(error => {
          console.error('Login failed:', error);
          errorMessage.value = 'Invalid username or password.';
        });
    };
const goToRegister = () => {
  router.push('/register');
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

.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

.login-form {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
  width: 300px;
}

.login-form h2 {
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

.login-button {
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

.login-button:hover {
  background-color: #2d9c55;
}

.register-button {
  margin-top: 1rem;
  background-color: #fff;
  color: #34B466;
  border: 1px solid #34B466;
  width: 100%;
  padding: 0.75rem;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.register-button:hover {
  background-color: #f5f5f5;
}

.error-message {
  color: red;
}
</style>