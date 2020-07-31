<template>
  <div class="ComponentImage">
    <swiper>
      <swiper-slide v-for="(image,index) in images" :key="index">
        <img v-bind:src="require('@/assets/img/' + image)" width="200" height="200">
      </swiper-slide>
    </swiper>

  </div>
</template>

<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.css'

export default {
  components: {
    Swiper,
    SwiperSlide
  },
  data() {
      return {
        images:['vessel-5.jpg','c97a9.jpg']
      }
}
}
</script>
<style lang="scss" scoped>
  @import '@/assets/style/base.scss';
</style>
