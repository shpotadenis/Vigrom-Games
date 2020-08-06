<template>
  <div class="wrappen">
    <div class="NewGamePageComponent">
      <div class="NewGameTitle">
        <p class="Title">Новинки</p>
      </div>
      <div class="NewsGamePage">
        <game-card
          v-for="gamebests in news"
          :key="gamebests.id"
          :Game="gamebests"
        />
      </div>
    </div>
  </div>
</template>

<script src="./NewGamePage.js">
</script>
<style lang="scss">
@import '@/assets/style/NewGamePage.scss'
</style>
