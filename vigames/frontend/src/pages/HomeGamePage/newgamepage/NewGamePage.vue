<template>
  <div class="wrappen">
    <div class="NewGamePageComponent">
      <div class="NewGameTitle">
        <p class="Title">Новинки</p>
        <a src="#1" class="Link">Больше игр <img src="@/assets/img/Vector.png"></a>
      </div>
      <div class="NewsGamePage">
        <new-game-page-component
        v-for="item in news"
        :key="item.id"
        :Game="item"
        />
      </div>
    </div>
  </div>
</template>

<script>

import NewGamePageComponent from "./NewGamePageComponents"

export default {
  name: 'NewGamePage',
  components: {
    NewGamePageComponent
  },
  data(){
  return{
    news:[
      {
      id:"1",
      image:"MaskGroup.svg",
      name:"DANGER CREW",
      rating:"4.9",
      undername:"Ubisoft Nadeo | Ubisoft",
      price:"299.99"
      },
      {
      id:"2",
      image:"MaskGroup.svg",
      name:"DANGER CREW",
      rating:"4.9",
      undername:"Ubisoft Nadeo | Ubisoft",
      price:"299.99"
      },
      {
      id:"3",
      image:"MaskGroup.svg",
      name:"DANGER CREW",
      rating:"4.9",
      undername:"Ubisoft Nadeo | Ubisoft",
      price:"299.99"
      },
      {
      id:"4",
      image:"MaskGroup.svg",
      name:"DANGER CREW",
      rating:"4.9",
      undername:"Ubisoft Nadeo | Ubisoft",
      price:"299.99"
      },
    ],
    

}
},
  props:{

  },
  methods:{

}

}
</script>
<style>
.NewGameTitle{
position:relative;
top:40px;
left:40px;
  display:flex;
  justify-content:space-between;
  width:1035px;
}
.Title{
  color:#fff;
  font-style: normal;
  font-weight: 800;
  font-size: 14px;
  text-transform:uppercase;
  line-height: 19px;
}
.Link{
  display:flex;
  justify-content:space-between;
  width:100px;
  font-style: normal;
  font-weight: 800;
  font-size: 14px;
  line-height: 19px;
  color: #7A7A83;

}
.NewGamePageComponent{
position:relative;
width: 1110px;
height: 515px;
margin-top:73px;
background: #2D2D42;
border-radius: 10px;
}
.NewsGamePage{
display:flex;
position:relative;
top:40px;
left:40px;
margin-right:25px;
width:1110px;
z-index:99999;

}
</style>
