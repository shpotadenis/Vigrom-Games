<template>
  <div>
<div class="wrappen">
<div class="FreeGames">
  <internal-menu/>
  <div class="FilterGames">
      <search-component/>
  </div>
</div>
<div class="FreeGamesTitle">
  <p class="Title">Бесплатные игры</p>
</div>
<banner-component day="Сегодня"
                  header="НОВЫЕ ИНДИ ИГРЫ УЖЕ НА ГЛАВНОЙ"
                  description="Унитарное государство, однако, доказывает системный политический процесс в современной России"
                  btn_caption="Подробнее"
                  :btn_route="{ name: 'homePage' }">
</banner-component>
  <div class="FreeGamesComponents">
    <game-card
    class="ItemCard"
    v-for="free in freegames"
    :key="free.id"
    :Game="free"
    />
  </div>


</div>
    <footer-component></footer-component>
  </div>
</template>


<script src="./FreeGames.js" type="application/javascript">
</script>

<style lang="scss" scoped>
@import "@/assets/style/FreeGames.scss";
</style>
