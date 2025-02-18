<template>
  <div>
    <h2>Notenverlauf</h2>
    <div style="height: 400px;">
      <!-- Canvas element for rendering the chart -->
      <canvas ref="chartCanvas"></canvas>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Chart from 'chart.js/auto';
import axios from 'axios';
import { BASE_URL } from '../config';

const chartCanvas = ref(null);

// Extract user ID from the JWT token
const getUserIdFromToken = (token) => {
  const base64Url = token.split('.')[1];
  const base64 = base64Url.replace('-', '+').replace('_', '/');
  const decodedData = JSON.parse(window.atob(base64));
  return decodedData.user_id;
};

// Fetch completed modules for the user
const fetchCompletedModules = async (userId) => {
  const token = localStorage.getItem('access_token');
  try {
    const response = await axios.get(`${BASE_URL}/api/users/${userId}/completed-modules/`, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });
    return response.data;
  } catch (error) {
    console.error('Error when retrieving the completed modules:', error);
    return [];
  }
};

// Process the fetched data to format it for Chart.js
const processChartData = (data) => {
  data.sort((a, b) => new Date(a.completion_date) - new Date(b.completion_date));
  const labels = [];
  const grades = [];
  const cumulativeAverages = [];
  let totalGrades = 0;
  data.forEach((item, index) => {
    const date = new Date(item.completion_date);
    const formattedDate = date.toLocaleDateString('de-DE');
    labels.push(formattedDate);
    grades.push(item.grade);
    totalGrades += parseFloat(item.grade);
    const cumulativeAverage = (totalGrades / (index + 1)).toFixed(2);
    cumulativeAverages.push(cumulativeAverage);
  });
  return {
    labels: labels,
    datasets: [
      {
        label: 'Grade',
        data: grades,
        borderColor: '#AE8DDF',
        backgroundColor: '#AE8DDF',
        fill: false,
        tension: 0.1
      },
      {
        label: 'Cumulative average',
        data: cumulativeAverages,
        borderColor: '#DFAE8D',
        backgroundColor: '#DFAE8D',
        fill: false,
        tension: 0.1
      }
    ]
  };
};

onMounted(async () => {
  const token = localStorage.getItem('access_token');
  const userId = getUserIdFromToken(token);
  const data = await fetchCompletedModules(userId);
  if (data && data.length > 0) {
    const chartDataProcessed = processChartData(data);
    const ctx = chartCanvas.value.getContext('2d');
    new Chart(ctx, {
      type: 'line',
      data: chartDataProcessed,
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: false,
            reverse: true,
            suggestedMin: 1,
            suggestedMax: 6,
            ticks: {
              stepSize: 0.5
            },
            title: {
              display: true,
              text: 'Grade'
            }
          },
          x: {
            title: {
              display: true,
              text: 'Date'
            }
          }
        }
      }
    });
  } 
});
</script>

<style scoped>
canvas {
  max-width: 100%;
  max-height: 100%;
}
</style>
