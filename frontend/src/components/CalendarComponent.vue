<template>
  <div class="calendar-container">
    <!-- v-calendar displays a calendar with highlighted appointments -->
    <v-calendar
      expanded
      is-expanded
      :attributes="attrs"
      @dayclick="handleDayClick"
    ></v-calendar>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { BASE_URL } from '../config';
import 'v-calendar/style.css';

// Define colors for different appointment categories
const categoryColors = {
  'PERS': '#AE8DDF',
  'ORG': '#DFAE8D',
  'EXM': '#FF6347',
};

const attrs = ref([]);

// Fetch appointments from the API and map them to calendar attributes
const fetchAppointments = async () => {
  const token = localStorage.getItem('access_token');
  try {
    const response = await axios.get(`${BASE_URL}/api/appointments/`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    // Map each appointment to an attribute for the calendar
    attrs.value = response.data.map((appointment) => {
      const backgroundColor = categoryColors[appointment.category] || '#AE8DDF';

      return {
        key: appointment.id,
        highlight: {
          contentStyle: {
            backgroundColor: backgroundColor,
            borderRadius: '50%',
          },
          style: {},
        },
        dates: new Date(appointment.scheduled_at),
        popover: {
          label: appointment.title,
        },
      };
    });
  } catch (error) {
    console.error('Error loading appointments:', error);
  }
};

// Handle click on a day in the calendar
const handleDayClick = ({ date }) => {
  alert(`Date clicked: ${date}`);
};

onMounted(() => {
  fetchAppointments();
});
</script>

<style>
.calendar-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}
</style>
