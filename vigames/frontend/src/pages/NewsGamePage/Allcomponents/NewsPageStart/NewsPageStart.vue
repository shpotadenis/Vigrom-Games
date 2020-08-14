<template>
<div>
  <div class="NewsSectionAndSearch">
    <div class="Block1">
      <p class="NewsSection">Новостной раздел</p>
    </div>
    <div class="Block2">
      <news-search searchzone="news" />
    </div>
    </div>

</div>
</template>


<script>

import NewsSearch from "@/components/SearchComponent/index.vue"

export default{
  name:"NewsPageStart",
  components:{
    NewsSearch
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
margin-bottom:60px;
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
