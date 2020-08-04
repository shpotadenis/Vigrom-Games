<template>
<div class="RecommendationGamePage">
  <div class="RecommedationGameTitle">
    <p class="Title">Рекомендации</p>
    <a src="#1" class="Link">Больше игр <img src="@/assets/img/Vector.png"></a>
  </div>
  <div class="RecommendationComponents">
    <game-card
      class="ItemCard"
      v-for="item in recommendation"
      :key="item.id"
      :Game="item"
    />
  </div>
</div>
</template>

<script src="./RecommendationGamePage.js">
</script>
<style lang='scss'>
@import '@/assets/style/RecommendationGamePage.scss'
</style>
