<template>
<div class="RecommendationGamePage">
  <div class="RecommedationGameTitle">
    <p class="Title">Рекомендации</p>
    <a src="#1" class="Link">Больше игр <img src="@/assets/img/Vector.png"></a>
  </div>
  <div class="RecommendationComponents">
    <little-popular-page-components
      v-for="item in recommendation"
      :key="item.id"
      :Game="item"
    />
  </div>
</div>
</template>

<script>

import LittlePopularPageComponents  from "../popularcomponents/LittlePopularPageComponents"

export default {
  name: 'RecommendationGamePage',
  components: {
    LittlePopularPageComponents
  },
  data(){
  return{
    recommendation:[
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
  }
}
</script>
<style>
.RecommendationGamePage{
margin-top:72px;
}
.RecommedationGameTitle{
display:flex;
justify-content:space-between;
}
.RecommendationComponents{
display:flex;
justify-content:space-between;
}
</style>
