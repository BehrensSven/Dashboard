<template>
  <div>
    <header>
      <nav>
        <ul>
          <li><a href="#dashboard">Dashboard</a></li>
          <li><a href="#kurse">Kurse</a></li>
          <li><a href="#news">News</a></li>
          <li><a href="#studium">Studium</a></li>
          <li><a href="#infos">Infos</a></li>
          <li class="logout-button"><button @click="logout">Logout</button></li>
        </ul>
      </nav>
    </header>

    <main>
      <section id="section1" class="section">Section 1</section>
      <section id="section2" class="section">Section 2</section>
      <section id="section3" class="section">Section 3</section>
      <section id="section4" class="section">Section 4</section>
    </main>

    <footer>
      <nav>
        <ul>
          <li><a href="#section1">Section 1</a></li>
          <li><a href="#section2">Section 2</a></li>
          <li><a href="#section3">Section 3</a></li>
          <li><a href="#section4">Section 4</a></li>
        </ul>
      </nav>
    </footer>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const logout = () => {
  localStorage.removeItem('accessToken');
  localStorage.removeItem('refreshToken');
  router.push('/login');
};
</script>

<style scoped>
header {
  background-color: whitesmoke;
  padding: 10px 0;
}

nav ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
}

nav ul li {
  margin: 0 15px;
}

nav ul li a {
  color: #34B466;
  text-decoration: none;
  font-weight: bold;
  transition: color 0.3s, text-shadow 0.3s;
}

nav ul li a:hover {
  color: #34B466;
  text-shadow: 0 0 10px rgba(52, 180, 102, 0.7);
}

.logout-button {
  margin-left: auto;
}

.logout-button button {
  background-color: #34B466;
  color: white;
  border: none;
  padding: 5px 10px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.logout-button button:hover {
  background-color: #2d9c55;
}

main {
  height: calc(100% - 80px);
  overflow-y: scroll;
}

.section {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 24px;
  border: 1px solid #ddd;
}

footer {
  background-color: #34B466;
  padding: 10px 0;
  position: fixed;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 50%;
  border-radius: 15px 15px 0 0;
}

footer nav ul {
  display: flex;
  justify-content: center;
}

footer nav ul li {
  margin: 0 15px;
}

footer nav ul li a {
  color: white;
  text-decoration: none;
  font-weight: bold;
  transition: color 0.3s, text-shadow 0.3s;
}

footer nav ul li a:hover {
  color: white;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.7);
}
</style>
