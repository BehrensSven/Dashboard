<template>
    <v-calendar
      is-expanded
      :attributes="attrs"
      @dayclick="handleDayClick"
    ></v-calendar>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import { BASE_URL } from '../config';
  import 'v-calendar/style.css';
  
  
  const attrs = ref([]);
  
  const fetchAppointments = async () => {
    const token = localStorage.getItem('access_token');
    try {
      const response = await axios.get(`${BASE_URL}/api/appointments/`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      attrs.value = response.data.map((appointment) => ({
        key: appointment.id,
        highlight: true,
        dates: new Date(appointment.scheduled_at),
        popover: {
          label: appointment.title,
        },
      }));
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
  </style>
  