<template>
  <div class="news-container">
    <div v-if="news.length">
      <div v-for="item in news" :key="item.id" class="news-item">
        <div>
          <img :src="getImageUrl(item.type)" alt="News Bild" class="news-image">
        </div>
        <div class="text">
          <h3 style="font-weight: medium; font-family: 'Roboto Slab', sans-serif;">{{ item.title }}</h3>
          <p style="font-weight: lighter; font-size: 0.9em; font-family: 'Roboto Slab', sans-serif;">{{ item.content }}</p>
          <small>Erstellt am: {{ new Date(item.created_at).toLocaleDateString() }}</small>
        </div>
      </div>
    </div>
    <div v-else>
      <p style="font-weight: lighter;">No news available</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { BASE_URL } from '../config'


const news = ref([])

const fetchNews = async () => {
  const token = localStorage.getItem('access_token');
  try {
    const response = await axios.get(`${BASE_URL}/api/news/`, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });
    news.value = response.data
  } catch (error) {
    console.error("Fehler beim Laden der News:", error)
  }
}

const getImageUrl = (type) => {
  switch (type) {
    case 'info':
      return `${BASE_URL}/static/info.svg`;
    case 'warnung':
      return `${BASE_URL}/static/warning.svg`;
    case 'support':
      return `${BASE_URL}/static/support.svg`;
    default:
  }
}

onMounted(fetchNews)
</script>

<style scoped>
.news-item {
  display: flex;
  align-items: center;
  border-bottom: 1px solid #ccc;
  margin-bottom: 15px;
  padding-bottom: 15px;
}

.news-image {
  width: 50px;
  height: 50px;
  margin-right: 10px;
}

.text {
  flex: 1;
}
</style>