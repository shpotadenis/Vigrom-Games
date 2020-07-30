<template>
<div class="CategoriesGamePage">
  <div class="PopularGameTitle">
    <p class="Title">Категории</p>
    <a src="#1" class="LinkCategories">Все категории <img src="@/assets/img/Vector.png"></a>
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

<script>

import CategoriesGamePageComponents from "./CategoriesGamePageComponents"

export default {
  name: 'CategoriesGamePage',
  components: {
    CategoriesGamePageComponents
  },
  data(){
    return{
      categories:[
      {
        name:"Экшен",
        image:"flash-icon.svg"
      },
      {
        name:"Симуляторы",
        image:"cube-icon.svg"
      },
      {
        name:"Стратегии",
        image:"map-icon.svg"
      },
      {
        name:"Инди",
        image:"smiling-face-outline.svg"
      },
      {
        name:"Приключения",
        image:"globe-icon.svg"
      },
      {
        name:"ММО",
        image:"shield-icon.svg"
      }
      ]
    }
  }
}
</script>
<style>
.LinkCategories{
display:flex;
justify-content:space-between;
width:120px;
font-style: normal;
font-weight: 800;
font-size: 14px;
line-height: 19px;
color: #7A7A83;
}
.AllComponentsCategories{
  display:flex;
  justify-content:space-between;
}
</style>
