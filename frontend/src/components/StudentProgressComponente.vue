<template>
    <div>
      <h1>Studienfortschritt</h1>
      <div v-if="loading">Lade Daten...</div>
      <div v-else-if="error">{{ error }}</div>
      <div v-else>
        <div class="progress-container">
          <p>Abgeschlossene Module: {{ modulesCompletedPercentage.toFixed(2) }}%</p>
          <div class="progress-bar">
            <div
              class="progress-fill"
              :style="{ width: modulesCompletedPercentage + '%' }"
            ></div>
          </div>
        </div>
  
        <div class="progress-container">
          <p>Studierte Zeit: {{ timeElapsedPercentage.toFixed(2) }}%</p>
          <div class="progress-bar">
            <div
              class="progress-fill time"
              :style="{ width: timeElapsedPercentage + '%' }"
            ></div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import { BASE_URL } from '../config';
  
  const progress = ref(null);
  const loading = ref(true);
  const error = ref(null);
  
  const modulesCompletedPercentage = ref(0);
  const timeElapsedPercentage = ref(0);
  
  async function fetchProgress() {
    try {
      const response = await axios.get(`${BASE_URL}/api/users/progress/`, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access_token')}`,
        },
      });
      progress.value = response.data;
  
      // Berechne die Prozentsätze
      if (progress.value.total_modules > 0) {
        modulesCompletedPercentage.value =
          (progress.value.modules_passed / progress.value.total_modules) * 100;
      } else {
        modulesCompletedPercentage.value = 0;
      }
  
      if (progress.value.standard_duration_days > 0) {
        timeElapsedPercentage.value =
          (progress.value.time_studied_days / progress.value.standard_duration_days) * 100;
      } else {
        timeElapsedPercentage.value = 0;
      }
  
      modulesCompletedPercentage.value = Math.min(modulesCompletedPercentage.value, 100);
      timeElapsedPercentage.value = Math.min(timeElapsedPercentage.value, 100);
    } catch (err) {
      error.value = 'Fehler beim Laden der Fortschrittsdaten.';
      console.error(err);
    } finally {
      loading.value = false;
    }
  }
  
  onMounted(() => {
    fetchProgress();
  });
  </script>
  
  <style scoped>
  .progress-container {
    margin-bottom: 20px;
  }

  .progress-container p {
  color: #000000a9;
  }
  
  .progress-bar {
    width: 100%;
    background-color: #75E0A0;
    border-radius: 10px;
    overflow: hidden;
    height: 20px;
    margin-top: 5px;
  }
  
  .progress-fill {
    height: 100%;
    background-color: #34B466;
    width: 0%;
    transition: width 0.5s ease-in-out;
  }
  
  .progress-fill.time {
    background-color: #34B466;
  }
  
  .raw-data p {
    margin: 5px 0;
  }
  </style>

