<template>
<div>
  <div class="NewsSectionAndSearch">
    <div class="Block1">
      <p class="NewsSection">Новостной раздел</p>
    </div>
    <div class="Block2">
      <img src="@/assets/img/search-icon.png" class="ImageSeach">
      <input
      type="text"
      placeholder="Поиск..."
      class="SearchNews"
      >
      <img src="@/assets/img/block.svg" class="SearchImage">
    </div>
    </div>
    <div class="BlockBaner">
      <div class="TextBaner">
        <p class="DateBaner">Сегодня</p>
        <p class="NameBaner">МЫ ОПУСКАЕМ ПЛАНКУ ВХОДА</p>
        <p class="UnderNameBaner">Унитарное государство, однако, доказывает системный политический процесс в современной России</p>
        <button class="ButtonBaner">Подробнее <img src="@/assets/img/Vector.png"></button>
      </div>
      <div>
        <img src="@/assets/img/902d1.svg" class="ImageBest">
      </div>
    </div>
</div>
</template>


<script>
export default{
  name:"NewsPageStart",
  components:{

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
.BlockBaner{
display:flex;
justify-content:space-between;
margin-top:61px;
width:1110px;
height:294px;
background: #2D2D42;
border-radius: 10px;
}
.DateBaner{
position:relative;
top:40px;
left:40px;
text-transform:uppercase;
font-style: normal;
font-weight: normal;
font-size: 14px;
line-height: 19px;
color: #7A7A83;
}
.NameBaner{
position:relative;
top:104px;
left:40px;
font-style: normal;
font-weight: bold;
font-size: 24px;
line-height: 28px;
color: #FFFFFF;
}
.UnderNameBaner{
position:relative;
top:110px;
left:40px;
width:411px;
font-style: normal;
font-weight: normal;
font-size: 14px;
line-height: 19px;
color: #7A7A83;
}
.ButtonBaner{
position:relative;
top:136px;
left:40px;
width: 139px;
height: 38px;
background: #CE6796;
border-radius: 6px;
border:none;
font-style: normal;
font-weight: 800;
font-size: 14px;
line-height: 19px;
color: #FFFFFF;
}
.ButtonBaner:hover{
    -moz-box-shadow:0 0 15px #CE6796;
    -webkit-box-shadow:0 0 15px #CE6796;
    box-shadow:0 0 15px #CE6796;
}
.ImageBest{
position:relative;
top:28px;
right:95px;
}
</style>
