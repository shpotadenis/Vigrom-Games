<template>
  <div class="wrapper">
  <div class="Slider" :style="{'margin-left': '-' + (100 * currentsSlideIndex) + '%' }">
    <popular-games-components
    v-for="item in Array_Slide"
    :key="item.id"
	:Game_Popular="item"
    />
    <div class="ImageVector1" @click="leftFunc">
      <img src="@/assets/img/Vector.svg" class="strelka1" @click="leftFunc" width="50" height="50">
    </div>
    <div class="ImageVector2" @click="rightFunc">
      <img src="@/assets/img/Vector.svg" class="strelka2" @click="rightFunc" width="50" height="50">
    </div>
  </div>

  </div>
</template>

<script src="./PopularGames.js">
</script>

<style lang='scss'>
@import "@/assets/style/PopularGames.scss"
</style>
