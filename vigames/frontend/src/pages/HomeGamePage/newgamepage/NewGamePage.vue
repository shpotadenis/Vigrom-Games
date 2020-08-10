<template>
  <div class="wrappen">
    <div class="NewGamePageComponent">
      <div class="NewGameTitle">
        <p class="Title">Новое</p>
      </div>
      <div class="NewsGamePage">
        <game-card
          v-for="gamebests in list"
          :key="gamebests.id"
          :Game="gamebests"
          class="game-card"
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
