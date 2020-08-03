<template>
<div class="container">
  <div class="col">
    <div class="wrappen">
      <categories/>
      <popular-games
        :Array_Slide="items"
        :Interval="4000"
      />
      <little-popular/>
      <new-game-page/>
      <bests-game-page/>
      <categories-game-page/>
      <recommendation-game-page/>
      <div class="Banner"></div>
      <div class="foot">
        <footer-components/>
      </div>
    </div>
  </div>
</div>
</template>

<script src="./HomePage.js">
</script>
<style lang="scss">
@import '@/assets/style/HomePage.scss'
</style>
