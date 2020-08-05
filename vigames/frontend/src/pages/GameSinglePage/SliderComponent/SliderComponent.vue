<template>
  <div class="wrapper">
    <div class="Slider" :style="{'margin-left': '-' + (100 * currentsSlideIndex) + '%' }">
      <slider-element
      v-for="(item, idx) in Array_Slide"
      :key="'slide' + idx"
      :Game_Popular="item"
      />

      <div v-if="Array_Slide.length > 1" class="ImageVector1" @click="leftFunc">
        <img src="@/assets/img/Vector.svg" class="strelka1"  width="50" height="50">
      </div>
      <div v-if="Array_Slide.length > 1" class="ImageVector2" @click="rightFunc">
        <img src="@/assets/img/Vector.svg" class="strelka2"  width="50" height="50">
      </div>
    </div>
  </div>
</template>

<script src="./SliderComponent.js">
</script>

<style scoped src="./SliderComponent.css">
</style>
