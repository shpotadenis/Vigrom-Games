<template>
<div>
<div class="SelectedArticles">
  <p class="SelectedArticlesDate">{{Selected_News.date}}</p>
  <p class="SelectedArticlesText">{{Selected_News.name}}</p>
</div>
</div>
</template>


<script>

export default{
  name:"SelectedArticles",
  components:{

  },
  props:{
    Selected_News:{
      type:Object,
      default(){
        return{}
      }
    }

  },
  data(){
    return{

    }
  }
}
</script>

<style scoped>
.SelectedArticles{
margin-top:25px;
width: 255px;
height: 255px;
background: #2D2D42;
border-radius: 10px;
}
.SelectedArticlesDate{
position:relative;
top:30px;
left:30px;
font-style: normal;
font-weight: normal;
font-size: 14px;
line-height: 19px;
text-transform:uppercase;
color: #FFFFFF;
}
.SelectedArticlesText{
position:relative;
left:30px;
top:130px;
width:195px;
height:75px;
font-style: normal;
font-weight: bold;
font-size: 18px;
line-height: 25px;
display: flex;
align-items: flex-end;
color: #FFFFFF;
}
</style>
