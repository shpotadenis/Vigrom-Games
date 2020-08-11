<template>
<div class="RecommendationGamePage" v-if="!loading">
  <div class="RecommedationGameTitle">
    <p class="Title">Рекомендации</p>
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
