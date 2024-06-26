<template>
  <div class="pt-14 flex justify-evenly w-full">
    <div v-if="cars.length && !loading">
      <div class="flex justify-center items-center flex-col">
        <h1 class="uppercase font-sans font-extralight lg:text-4xl md:text-4xl text-2xl mt-16 text-center">Search results</h1>
        <span class="mt-4">Found {{ this.cars.length }} result</span>
      </div>
      <div class="grid xl:grid-cols-4 lg:grid-cols-3 md:grid-cols-2 sm:grid-cols-2 gap-x-16 gap-y-20 mt-16">
        <div v-for="car in cars" :key="car.id" class="max-w-[280px] h-[350px] shadow-2xl z-1 w-full flex flex-col justify-start bg-[#E6E6E6] rounded-xl reveal-car">
          <router-link :to="Trans.i18nRoute({ name: 'cardetail', params: {'id': car.id} })" class="w-full bg-black rounded-t-xl flex justify-center overflow-hidden">
            <img v-if="car.main_image" :src="car.main_image.image_url" class="h-44 w-[99%] object-contain rounded-t-xl transition-transform transform hover:scale-105 cursor-pointer" alt="">
          </router-link>
          <hr class="h-px bg-black border-0">
          <span class="uppercase text-[10px] mt-2 ml-2 mb-2">{{ car.location }}</span>
          <router-link :to="Trans.i18nRoute({ name: 'cardetail', params: {'id': car.id} })">
            <span class="whitespace-nowrap overflow-hidden overflow-ellipsis cursor-pointer ml-2 uppercase text-lg text-gray-900 hover:text-red-900 font-semibold">{{ car.manufacturer }} - <span class="font-light text-black">{{ car.car_model }}</span></span>
          </router-link>
          <span class="uppercase font-light mt-4 ml-2 text-gray-900">{{ car.price }} <span class="font-semibold">$</span></span>
          <hr class="h-px mt-7 bg-black border-0">
          <div class="flex flex-row mt-2 ml-2">
            <span class="uppercase text-[10px] p-2 bg-black text-white rounded-full px-3">{{ car.created_by.name }}</span>
            <span class="uppercase text-[10px] p-2 bg-black text-white rounded-full px-3 ml-2">{{ car.types }}</span>
          </div>
        </div>
      </div>
    </div>
    <div v-else-if="!cars.length && loading">
      <h1 class="uppercase font-sans font-extralight lg:text-4xl md:text-4xl text-2xl mt-16 text-center">Loading...</h1>
      <div class="grid xl:grid-cols-4 lg:grid-cols-3 md:grid-cols-2 sm:grid-cols-2 gap-x-16 gap-y-20 mt-16">
        <div v-for="index in 8" :key="index" class="border w-[300px] border-gray-200 p-4">
          <div class="animate-pulse space-y-2">
            <div class="bg-[#222] rounded-lg h-48"></div>
            <div class="flex-1 space-y-2">
              <div class="h-16 bg-[#222] rounded-lg w-full"></div>
              <div class="space-x-2 flex">
                <div class="h-8 bg-[#222] rounded-lg w-full"></div>
                <div class="h-8 bg-[#222] rounded-lg w-full"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="flex justify-center items-center flex-col">
      <h1 class="uppercase font-sans font-extralight lg:text-4xl md:text-4xl text-2xl mt-10">Results not found!!!</h1>
      <span class="mt-4">Found {{ this.cars.length }} result</span>
      <img src="/not-found.png" alt="not-found" class="w-[800px]">
    </div>
  </div>
</template>

<script>
import { RouterLink } from 'vue-router'
import axios from 'axios'
import Trans from '@/i18n/translation'
export default {
setup() {
  return {
    Trans
  }
},
data() {
  return {
    query: this.$route.query.q || '',
    loading: false,
    cars: []
  }
},
watch: {
$route(to, from) {
  this.query = to.query.q || '';
  this.fetchSearchResults();
},
},
methods: {
fetchSearchResults() {
  const params = this.$route.query
  this.loading = true
  axios.get('/api/filters/', { params })
    .then(response => {
      this.cars = response.data
    })
    .catch(error => {
      console.error('Error fetching search results:', error);
    })
    .finally(() => {
      this.loading = false
    })
  },
  setPageTitle(title) {
      document.title = title
  }
},
mounted() {
  this.fetchSearchResults(),
  this.setPageTitle('Search Results');
}
}
</script>