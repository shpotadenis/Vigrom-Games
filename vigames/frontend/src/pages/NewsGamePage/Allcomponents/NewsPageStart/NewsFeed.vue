<template>
<div class="NewsFeedComponents">
  <div class="NewsFeedComponents">
    <img v-bind:src="require('@/assets/img/' + News_Feed.image)" width="520" height="324">
    <div class="NewsFeedTextAndImage">
      <p class="NewsFeedName">{{News_Feed.name}}</p>
      <img src="@/assets/img/Vector.svg" class="NewsFeedTextAndImageImg">
    </div>
    <p class="NewsFeedUnderName">{{News_Feed.undername}}</p>
  </div>
</div>
</template>


<script>



export default{
  name:"NewsFeed",
  components:{

  },
  props:{
    News_Feed:{
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
.NewsFeedComponents{
display: inline-block;
  width: 540px;
  height: 324px;
margin-top:25px;
margin-right:15px;

}
.NewsFeedName{
margin-top:20px;
font-style: normal;
font-weight: bold;
font-size: 18px;
line-height: 25px;
color: #FFFFFF;
}
.NewsFeedTextAndImage{
display:flex;
justify-content:space-between;
width:520px;
}
.NewsFeedTextAndImageImg{
position:relative;
top:10px;
left:-10px;
}
.NewsFeedUnderName{
margin-top:3px;
font-style: normal;
font-weight: normal;
font-size: 14px;
line-height: 19px;
color: #7A7A83;
}
</style>
