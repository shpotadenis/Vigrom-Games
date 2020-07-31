<template>
  <div class="wrappen">
      <div class="GameComponent">
      <div class="ImagePopular">
        <img v-bind:src="require('@/assets/img/' + Game.image)" wigth="255" height="324">
      </div>
        <div class="RatingAndTitle">
          <p class="NameGame">{{Game.name}}</p>
          <div class="RatingGame">{{Game.rating}}</div>
        </div>
        <p class="UnderName">{{Game.undername}}</p>
        <p class="Price">{{Game.price}}</p>
      </div>

  </div>
</template>

<script>


export default {
name: 'LittlePopularPageComponents',
components: {

},
props:{
  Game:{
  type:Object,
  default(){
    return{}
  }
}
}
}

</script>

<style>
.GameComponent{
  position:relative;
  display:inline-block;
  margin-top:25px;
  margin-right:30px;

}
.RatingAndTitle{
  display:flex;
  justify-content:space-between;
  padding-top:24px;

}
.ImagePopular{
overflow:hidden;
wigth:255px;
height:324px;
}
.ImagePopular img {
 -moz-transition: all 1s ease-out;
 -o-transition: all 1s ease-out;
 -webkit-transition: all 1s ease-out;
 }

.ImagePopular img:hover{
 -webkit-transform: scale(1.1);
 -moz-transform: scale(1.1);
 -o-transform: scale(1.1);
 }
.NameGame{
position:relative;
left:0;font-style: normal;
font-weight: 800;
font-size: 14px;
line-height: 19px;
}
.RatingGame{
width:35px;
height:18px;
text-align: center;
font-weight: 800;
font-size: 10px;
line-height: 14px;
color:#fff;
border: 2px solid #23B929;
box-sizing: border-box;
border-radius: 10px;
}
.UnderName{
font-style: normal;
font-weight: normal;
font-size: 14px;
line-height: 19px;
color: #7A7A83;
}
.Price{
font-style: normal;
margin-top:10px;
font-weight: normal;
font-size: 18px;
line-height: 25px;
color: #FFFFFF;

}
</style>
