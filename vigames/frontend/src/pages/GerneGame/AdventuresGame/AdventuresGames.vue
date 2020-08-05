<template>
  <div>
<div class="wrappen">
<div class="AdventuresGames">
  <internal-menu/>
  <div class="FilterGames">
      <search-component/>
  </div>
</div>
<div class="AdventuresGamesTitle">
  <p class="Title">Приключения</p>
</div>

  <div class="AdventuresGamesComponents">
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


<script src="./AdventuresGame.js" type="application/javascript">
</script>

<style lang="scss" scoped>
@import "@/assets/style/AdventuresGame.scss";
</style>
