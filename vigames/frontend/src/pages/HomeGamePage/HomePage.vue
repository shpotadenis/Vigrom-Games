<template>
  <div>
<div class="container">
  <div class="col">
    <div class="wrappen">
      <categories/>
      <popular-games
        :Array_Slide="items"
      />
      <little-popular/>
      <new-game-page/>
      <bests-game-page/>
      <categories-game-page/>
      <recommendation-game-page/>
      <div class="Banner"></div>
      <div class="foot">

      </div>
    </div>
  </div>
</div>
  <footer-components/>
</div>
</template>

<script src="./HomePage.js">
</script>
<style lang="scss">
@import '@/assets/style/HomePage.scss'
</style>
