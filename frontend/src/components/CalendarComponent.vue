<template>
    <div class="calendar-container">
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
  
  const categoryColors = {
    'PERS': '#AE8DDF',
    'ORG': '#DFAE8D',
    'EXM': '#FF6347',
  };
  
  const attrs = ref([]);
  
  const fetchAppointments = async () => {
    const token = localStorage.getItem('access_token');
    try {
      const response = await axios.get(`${BASE_URL}/api/appointments/`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
  
      attrs.value = response.data.map((appointment) => {
        const backgroundColor = categoryColors[appointment.category] || '#AE8DDF';
  
        return {
          key: appointment.id,
          highlight: {
            contentStyle: {
              backgroundColor: backgroundColor,
              borderRadius: '50%',
            },
            style: {
            },
          },
          dates: new Date(appointment.scheduled_at),
          popover: {
            label: appointment.title,
          },
        };
      });
    } catch (error) {
      console.error('Fehler beim Laden der Termine:', error);
    }
  };
  
  const handleDayClick = ({ date }) => {
    alert(`Datum angeklickt: ${date}`);
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
  