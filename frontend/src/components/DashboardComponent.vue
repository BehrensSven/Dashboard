<template>
  <div>
    <header>
      <nav>
        <ul>
          <li><a href="#news-section">Dashboard</a></li>
          <li><a href="#course-section">Kurse</a></li>
          <li><a href="#section3">News</a></li>
          <li><a href="#section4">Studium</a></li>
          <li><a href="#section5">Infos</a></li>
          <li class="spacer"></li>
          <li class="logout-button"><button @click="logout">Logout</button></li>
        </ul>
      </nav>
    </header>

    <main>
      <div class="dashboard-grid">
        <section id="news-section" class="dashboard-tile">
          <NewsComponent />
        </section>
        <section id="course-section" class="dashboard-tile">
          <CourseComponent />
        </section>
        <section id="section3" class="dashboard-tile">Section 3</section>
        <section id="section4" class="dashboard-tile">Section 4</section>
        <section id="section5" class="dashboard-tile">Section 5</section>
      </div>
    </main>

    <footer>
      <nav>
        <ul>
          <li><a href="#news-section">Section 1</a></li>
          <li><a href="#course-section">Section 2</a></li>
          <li><a href="#section3">Section 3</a></li>
          <li><a href="#section4">Section 4</a></li>
          <li><a href="#section5">Section 5</a></li>
        </ul>
      </nav>
    </footer>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import NewsComponent from './NewsComponent.vue';
import CourseComponent from './CourseComponent.vue';

const router = useRouter();

const logout = () => {
  localStorage.removeItem('accessToken');
  localStorage.removeItem('refreshToken');
  router.push('/login');
};
</script>

<style scoped>
html {
  scroll-behavior: smooth;
}

header {
  background-color: whitesmoke;
  padding: 10px 0;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 1000;
}

nav ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
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

.spacer {
  flex-grow: 1;
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
  padding-top: 60px;
}

.dashboard-grid {
  display: grid;
  margin: 10px 25px 10px 25px;
  grid-template-columns: 1fr;
  grid-gap: 20px;
}

.dashboard-tile {
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  transition: box-shadow 0.3s ease;
}

.dashboard-tile:hover {
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
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

#news-section {
  background-color: #D9D9D9;
}

#course-section {
  background-color: #D9D9D9;
}
</style>