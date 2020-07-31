<template>
  <div class="PopularGameIndi">
    <div class="PopularGameTitle">
      <p class="Title">Популярное</p>
      <a src="#1" class="Link">Больше игр <img src="@/assets/img/Vector.png"></a>
    </div>
    <div class="IndiPopularGame">
      <little-popular-page-components
        v-for="item in populars"
        :key="item.id"
        :Game="item"
      />
      </div>
  </div>
</template>

<script>

import LittlePopularPageComponents from "./LittlePopularPageComponents"

export default {
name: 'LittlePopularPage',
components: {
  LittlePopularPageComponents

},
data(){
return{
  populars:[
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
  ]
}
},

}
</script>

<style>
.PopularGameTitle{
  display:flex;
  justify-content:space-between;
  margin-top:100px;
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
.IndiPopularGame{
  display:flex;
}
</style>
