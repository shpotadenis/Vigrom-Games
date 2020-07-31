<template>

        <div class="GameComponent">
          <div class="ImageNewGame">
              <div class="rotate">
                <img class="ImageComponent" v-bind:src="require('@/assets/img/' + Game.image)">
                <div class="TextNewGame">
                  <div class="SlideBarImage">
                    <new-game-image
                    />
                  </div>
                  <p class="TextComponent">vnevnjehvnjiehv kjadb uib jab s sH YU</p>
                </div>
            </div>
          </div>
          <div class="RatingAndTitle">
            <p class="NameGame">{{Game.name}}</p>
            <div class="RatingGame">{{Game.rating}}</div>
          </div>
          <p class="UnderName">{{Game.undername}}</p>
          <p class="Price">{{Game.price}}</p>
        </div>


</template>

<script>

import NewGameImage from "./NewGameImage"

export default {
name: 'LittlePopularPageComponents',
components: {
NewGameImage
},
props:{
  Game:{
  type:Object,
  default(){
    return{}
  }
},
}
}


</script>
<style>
.GameComponent{
  position:relative;
  display:inline-block;
  padding-top:25px;

}
.RatingAndTitle{
  display:flex;
  justify-content:space-between;
  padding-top:24px;
  z-index:99999;
}
.SlideBarImage{
display:flex;
}
.ImageNewGame{
overflow:hidden;
wigth:235px;
height:301px;
perspective:1000px;
}
 .ImageNewGame:hover .rotate{
 transition-delay:1.2s;
transform: rotateY(180deg);
}
.rotate{
position:relative;
transition: 0.5s;
transform-style:preserve-3d;
}
.TextNewGame{
position:absolute;
top:0;
left:0;
font-style: normal;
font-weight: normal;
font-size: 14px;
line-height: 19px;
color: #fff;
transform: rotateY(180deg);
}
.TextComponent{
position:absolute;
top:200px;
left:27px;
width:180px;
text-align:center;
}
.ImageComponent{
vertical-aling:middel;
}
.ImageComponent,
.TextNewGame{
width:235px;
height:301px;
background:#212130;
backface-visibility:hidden;
}
.ImageNewGame,
.ImageComponent{
 -moz-transition: all 1s ease-out;
 -o-transition: all 1s ease-out;
 -webkit-transition: all 1s ease-out;
 }

.ImageNewGame .ImageComponent:hover{
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
