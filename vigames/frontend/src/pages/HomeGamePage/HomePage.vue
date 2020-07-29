<template>
  <div class="wrappen">
    <categories/>
    <popular-games/>
  </div>
</template>

<script>

import Categories from "./startcomponents/Categories"
import PopularGames from "./catalogscomponents/PopularGames"

export default {
  name: 'HomePage',
  components: {
    Categories,
    PopularGames
  }
}
</script>

<style>
.wrappen{
  width:1000px;
  margin:auto;
}
</style>