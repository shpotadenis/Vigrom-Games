<template>
  <div class="wrapper">
  <div class="Slider" :style="{'margin-left': '-' + (100 * currentsSlideIndex) + '%' }">
    <popular-games-components
    v-for="item in Array_Slide"
    :key="item.id"
	:Game_Popular="item"
    />
    <img src="@/assets/img/arrow3.png" class="strelka1" @click="leftFunc">
    <img src="@/assets/img/arrow3.png" class="strelka2" @click="rightFunc">
  </div>

  </div>
</template>

<script src="./PopularGames.js">
</script>

<style lang='scss'>
@import "@/assets/style/PopularGames.scss"
</style>
