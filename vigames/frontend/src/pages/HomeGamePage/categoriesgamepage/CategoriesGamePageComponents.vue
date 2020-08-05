<template>
<div>
  <top-category v-if="isBtnClick" @close="isBtnClick = false"/>
  <a @click="isBtnClick = true">
    <div class="CategoriesGamePageComponent">
      <img v-bind:src="require('@/assets/img/' + Categories_Game.image)" class="ImageCategories">
      <p class="TitleCategories">{{Categories_Game.name}}</p>
    </div>
  </a>
</div>
</template>

<script src="./CategoriesGamePageComponents.js">

</script>


<style lang="scss">
@import '@/assets/style/CategoriesGamePageComponents.scss'
</style>
