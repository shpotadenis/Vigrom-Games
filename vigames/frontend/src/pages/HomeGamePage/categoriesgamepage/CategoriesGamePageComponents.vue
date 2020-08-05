<template>
<div>
  <top-category v-if="isBtnClick" @close="isBtnClick = false"/>
  <a @click="isBtnClick = true">
  <div class="AllCategories">
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/flash-icon.svg" class="ImageCategories">
      <p class="TitleCategories">Экшен</p>
    </div>
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/cube-icon.svg" class="ImageCategories">
      <p class="TitleCategories">Симуляторы</p>
    </div>
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/map-icon.svg" class="ImageCategories">
      <p class="TitleCategories">Стратегии</p>
    </div>
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/smiling-face-outline.svg" class="ImageCategories">
      <p class="TitleCategories">Казуальные</p>
    </div>
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/globe-icon.svg" class="ImageCategories">
      <p class="TitleCategories">Приключения</p>
    </div>
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/shield-icon.svg" class="ImageCategories">
      <p class="TitleCategories">ММО</p>
    </div>
  </div>
  </a>
</div>
</template>

<script src="./CategoriesGamePageComponents.js">

</script>


<style lang="scss">
@import '@/assets/style/CategoriesGamePageComponents.scss'
</style>
