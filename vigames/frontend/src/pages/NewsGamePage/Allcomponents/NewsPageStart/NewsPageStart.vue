<template>
<div>
  <div class="NewsSectionAndSearch">
    <div class="Block1">
      <p class="NewsSection">Новостной раздел</p>
    </div>
    <div class="Block2">
      <search-component/>
    </div>
    </div>
    <banner-component day="Сегодня"
                      header="НОВЫЕ ИНДИ ИГРЫ УЖЕ НА ГЛАВНОЙ"
                      description="Унитарное государство, однако, доказывает системный политический процесс в современной России"
                      btn_caption="Подробнее"
                      :btn_route="{ name: 'homePage' }">
    </banner-component>
</div>
</template>


<script>

import BannerComponent from "@/components/BannerComponent/index.vue"
import SearchComponent from "@/components/SearchComponent/index.vue"

export default{
  name:"NewsPageStart",
  components:{
    BannerComponent,
    SearchComponent
  },
  props:{},
  data(){
    return{

    }
  }
}
</script>

<style scoped>
.NewsSectionAndSearch{
display:flex;
justify-content:space-between;
margin-bottom:25px;
}
.NewsSection{
position:relative;
top:10px;
font-style: normal;
font-weight: 800;
font-size: 14px;
line-height: 19px;
text-transform:uppercase;
color: #FFFFFF;
}

.SearchNews{
background-color:#212130;
border:none;
position:relative;
left:30px;
}
.ImageSeach{
position:relative;
top:-5px;
left:20px;
}
.SearchImage{
position:relative;
top:9px;


}

</style>
