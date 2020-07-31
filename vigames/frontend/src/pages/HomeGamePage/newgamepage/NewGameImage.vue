<template>
  <div class="ComponentImage">
    <img
    src="@/assets/img/vessel-5.jpg"
    class="ImageSlideBar"
    width="200" height="200"
    >

  </div>
</template>

<script>


export default {
name: 'NewGameImage',
components: {

},
props:{
  Game_Image:{
    type:Object,
    default(){
      return{}
    }
  }

}
}

</script>
<style>
.ComponentImage{
display:flex;
}
.ImageSlideBar{
margin-left:20px;
width:200px;
height:200px;
}

</style>
