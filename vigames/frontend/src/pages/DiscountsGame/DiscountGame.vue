<template>
  <div>
<div class="wrappen">
<div class="DiscountGames">
  <internal-menu/>
  <div class="FilterGames">
      <search-component/>
  </div>
</div>
<div class="DiscountGamesTitle">
  <p class="Title">Скидки</p>
</div>

  <div class="DiscountGamesComponents">
    <game-card
    class="ItemCard"
    v-for="discount in discountgames"
    :key="discount.id"
    :Game="discount"
    />
  </div>

</div>
    <footer-component></footer-component>
  </div>
</template>


<script src="./DiscountsGame.js" type="application/javascript">
</script>

<style lang="scss" scoped>
@import "@/assets/style/DiscountsGame.scss";
</style>
