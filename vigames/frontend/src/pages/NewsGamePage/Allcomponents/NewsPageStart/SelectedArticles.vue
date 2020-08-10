<template>
<div>
<div class="SelectedArticles">
  <p class="SelectedArticlesDate">{{getFormattedDate}}</p>
  <router-link :to="{name: 'newsSinglePage', params: {id: Selected_News.id}}">
    <p class="SelectedArticlesText">{{Selected_News.title}}</p>
  </router-link>
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
  },
  computed : {
    getFormattedDate() {
      let date = new Date(this.Selected_News.date);
      return new Intl.DateTimeFormat('ru-RU', { day: '2-digit', month: 'long',  year: 'numeric' }).format(date)
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
