<template>
  <div class="wrappen">
      <div class="GameComponentPopular">
      <div class="ImagePopular">
        <img class="ImageComponentPopular" v-bind:src="Game.image" wigth="255" height="324">
      </div>
        <div class="RatingAndTitlePopular">
          <router-link :to="{ name: 'singlePage', params: { id: Game.id } }">
              <p class="NameGamePopular">{{Game.name}}</p>
          </router-link>
          <p class="PricePopular">{{Game.price}}</p>
        </div>
        <p class="UnderNamePopular">{{Game.undername}}</p>
    </div>
</div>
</template>

<script src='./GameCard.js'>
</script>

<style lang='scss'>
@import '@/assets/style/GameCard.scss'
</style>
