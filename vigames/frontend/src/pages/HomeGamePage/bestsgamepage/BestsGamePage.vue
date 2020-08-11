<template>

  <div class="BestsGamePage" v-if="!loading">
    <div class="BestsGameTitle">
      <p class="Title">Бестселлеры</p>
    </div>
    <!-- <bests-game-page-components
      v-for="game in bests"
      :key="game.image"
      :Bests_Game="game"
    /> !-->
    <div class="BestsGameComponents">
      <game-card
        v-for="gamebests in bestscomponents"
        :key="gamebests.id"
        :Game="gamebests"
      />
    </div>

</div>
</template>

<script src="./BestGamePage.js" type="application/javascript">
</script>
<style lang="scss">
@import '@/assets/style/BestGamePage.scss'
</style>
