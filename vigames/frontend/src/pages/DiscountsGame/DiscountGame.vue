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
  <p class="Title">Бесплатные игры</p>
</div>
<banner-component day="Сегодня"
                  header="НОВЫЕ ИНДИ ИГРЫ УЖЕ НА ГЛАВНОЙ"
                  description="Унитарное государство, однако, доказывает системный политический процесс в современной России"
                  btn_caption="Подробнее"
                  :btn_route="{ name: 'homePage' }">
</banner-component>
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
