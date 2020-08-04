<template>
<div class="CategoriesGamePage">
  <div class="PopularGameTitle">
    <p class="Title">Популярные категории</p>
  
  </div>
  <div class="AllComponentsCategories">
    <categories-game-page-components
      v-for="item in categories"
      :key="item.name"
      :Categories_Game="item"
    />
  </div>
</div>
</template>

<script src="./CategoriesGamePage.js">

</script>
<style lang="scss">
@import '@/assets/style/CategoriesGamePage.scss'
</style>
