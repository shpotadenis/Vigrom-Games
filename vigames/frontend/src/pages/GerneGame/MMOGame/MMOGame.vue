<template>
  <div>
<div class="wrappen">
<div class="MMOGames">
  <internal-menu/>
  <div class="FilterGames">
      <search-component/>
  </div>
</div>
<div class="MMOGamesTitle">
  <p class="Title">Массовые многопользовательские игры</p>
</div>
  <div class="MMOGamesComponents">
    <game-card
    class="ItemCard"
    v-for="free in freegames"
    :key="free.id"
    :Game="free"
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


<script src="./MMOGame.js" type="application/javascript">
</script>

<style lang="scss" scoped>
@import "@/assets/style/MMOGame.scss";
</MMO
