<template>
  <div class="CategoriesGamePageComponent">
    <img v-bind:src="require('@/assets/img/' + Categories_Game.image)" class="ImageCategories">
    <p class="TitleCategories">{{Categories_Game.name}}</p>
  </div>
</template>

<script>

export default {
  name: 'CategoriesGamePageComponent',
  components: {
  },
  props:{
    Categories_Game:{
      type:Object,
      default(){
        return{}
      }
    }
  }

}
</script>
<style>
.CategoriesGamePageComponent{
position:relative;
width: 145px;
height: 170px;
background: #2D2D42;
border-radius: 10px;
margin-top:25px;
transition:all ease 0.3s;
}
.CategoriesGamePageComponent:hover{
background:#CE6796;

}
.ImageCategories{
position:absolute;
top:28%;
left:38.75%;
}
.TitleCategories{
  position:absolute;
  top:63%;
  width:145px;
  text-align:center;
}
</style>
