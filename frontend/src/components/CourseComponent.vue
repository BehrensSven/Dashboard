<template>
  <div class="course-container">
    <div class="toggle-container">
      <label class="switch">
        <input type="checkbox" v-model="isActive" @change="filterCourses">
        <span class="slider round"></span>
      </label>
      <span class="option">{{ isActive ? 'Bestanden' : 'Aktiv' }}</span>
    </div>

    <p v-if="loading">Loading courses...</p>
    
    <p v-if="error">{{ error }}</p>
    
    <div class="course-list" v-if="filteredCourses && filteredCourses.length">
      <div 
        v-for="course in filteredCourses" 
        :key="course?.id"
        class="course-item"
      >
        <button class="course-button">{{ course?.name }}</button>
      </div>
    </div>

    <p v-else>No courses available</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { BASE_URL } from '../config';

const courses = ref([]);
const filteredCourses = ref([]);
const loading = ref(true);
const error = ref('');
const isActive = ref(false);

const fetchCourses = async () => {
  const token = localStorage.getItem('access_token');

  try {
    const response = await axios.get(`${BASE_URL}/api/users/modules/`, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });
    courses.value = response.data;
    filterCourses();
  } catch (err) {
    error.value = "Error fetching courses";
  } finally {
    loading.value = false;
  }
};

const filterCourses = () => {
  if (isActive.value) {
    filteredCourses.value = courses.value.filter(course => !course.is_active);
  } else {
    filteredCourses.value = courses.value.filter(course => course.is_active);
  }
};

onMounted(fetchCourses);
</script>

<style scoped>
.course-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  width: 100%;
  height: 100%;
  padding: 20px;
}

.toggle-container {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  margin-bottom: 20px;
}

.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #A3D9A5;
  transition: .4s;
  border-radius: 34px;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  transition: .4s;
  border-radius: 50%;
}

input:checked + .slider {
  background-color: #ccc;
}

input:checked + .slider:before {
  transform: translateX(26px);
}

.option {
  font-size: 16px;
  font-weight: bold;
  color: black;
  margin-left: 15px;
  user-select: none;
}

.course-list {
  display: flex;
  flex-direction: column;
  max-height: 300px;
  overflow-y: auto;
  width: 95%;
  padding-right: 15px;
}

.course-list::-webkit-scrollbar {
  width: 10px;
}

.course-list::-webkit-scrollbar-thumb {
  background-color: #A3D9A5;
  border-radius: 10px;
  margin-left: 10px;
}

.course-item {
  margin-bottom: 20px;
  width: 100%;
}

.course-button {
  width: 100%;
  padding: 15px;
  background-color: #A3D9A5;
  border: none;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: left;
  font-size: 16px;
  cursor: pointer;
}

.course-button:active {
  background-color: #A3D9A5;
}
</style>
