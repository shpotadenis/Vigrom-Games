<template>
  <div>
<div class="wrappen">
<div class="EarlyAccessGames">
  <internal-menu/>
  <div class="FilterGames">
    <search-component></search-component>
  </div>
</div>
<div class="EarlyAccessGamesTitle">
  <p class="Title">Ранний доступ</p>
</div>

  <div class="EarlyAccessGamesComponents">
    <game-card
    class="ItemCard"
    v-for="discount in discountgames"
    :key="discount.id"
    :Game="discount"
    />
  </div>
  <banner-component day="Сегодня"
                    header="НОВЫЕ ИНДИ ИГРЫ УЖЕ НА ГЛАВНОЙ"
                    description="Унитарное государство, однако, доказывает системный политический процесс в современной России"
                    btn_caption="Подробнее"
                    :btn_route="{ name: 'homePage' }">
  </banner-component>
</div>
    <footer-component></footer-component>
  </div>
</template>


<script src="./EarlyAccessGame.js" type="application/javascript">
</script>

<style lang="scss" scoped>
@import "@/assets/style/EarlyAccessGame.scss";
</style>
