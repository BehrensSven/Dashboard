<template>
  <div class="container">
    <NavbarComponent />
    <HeaderComponent />
    <main class="main-content">
      <DashboardComponent />
    </main>
    <FooterComponent />
  </div>
</template>

<script setup>
import NavbarComponent from './components/NavbarComponent.vue';
import HeaderComponent from './components/HeaderComponent.vue';
import DashboardComponent from './components/DashboardComponent.vue';
import FooterComponent from './components/FooterComponent.vue';
</script>

<style>
.container {
  display: grid;
  grid-template-areas: 
    "navbar header"
    "navbar main"
    "navbar footer";
  grid-template-rows: auto 1fr auto;
  grid-template-columns: 200px 1fr;
  height: 100vh;
}

nav {
  grid-area: navbar;
}

header {
  grid-area: header;
}

.main-content {
  grid-area: main;
  padding: 20px;
}

footer {
  grid-area: footer;
}
</style>
