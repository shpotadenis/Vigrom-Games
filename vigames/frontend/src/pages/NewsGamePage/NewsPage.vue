<template>
<div class="container">
	<div class="col">
		<div class="NewsWrappen">
			<news-page-start/>
			<div class="SelectedArticlesText">
				<p class="SelectedArticlesTitle">ИЗБРАННЫЕ СТАТЬИ</p>
				<div class="SelectedArticlesComp">
					<selected-articles
						v-for="articles in Selected"
						:key="articles.id"
						:Selected_News="articles"
					/>
				</div>
			</div>
			<div class="NewsFeedText">
				<p class="NewsFeedTitle">НОВОСТНАЯ ЛЕНТА</p>
				<div class="NewsFeed">
					<news-feed
						v-for="news in Feeds"
						:key="news.id"
						:News_Feed="news"
					/>
				</div>
			</div>
			<div class="foot">
				<footer-component></footer-component>
			</div>
			</div>
	</div>
</div>
</template>


<script>

import NewsPageStart from "./Allcomponents/NewsPageStart/NewsPageStart.vue"
import SelectedArticles from "./Allcomponents/NewsPageStart/SelectedArticles.vue"
import NewsFeed from "./Allcomponents/NewsPageStart/NewsFeed.vue"
import FooterComponent from "../../components/FooterComponent/index.vue"


export default{
  name:"NewsPage",
  components:{
    NewsPageStart,
		SelectedArticles,
		NewsFeed,
    FooterComponent
  },
  props:{},
  data(){
    return{
			Selected:[
			{
				date:"Сегодня",
				name:"Новое оборудование на серверах Vigrom",
				id:"1"
			},
			{
				date:"Сегодня",
				name:"Новое оборудование на серверах Vigrom",
				id:"2"
			},
			{
				date:"Сегодня",
				name:"Новое оборудование на серверах Vigrom",
				id:"3"
			},
			{
				date:"Сегодня",
				name:"Новое оборудование на серверах Vigrom",
				id:"4"
			},
			],
			Feeds:[
			{
				id:"1",
				image:"image.svg",
				name:"Новое оборудование на серверах Vigrom",
				undername:"Как известно, политический процесс в современной России неравномерен. Типология средств..."
			},
			{
				id:"2",
				image:"image.svg",
				name:"Новое оборудование на серверах Vigrom",
				undername:"Как известно, политический процесс в современной России неравномерен. Типология средств..."
			},
			{
				id:"3",
				image:"image.svg",
				name:"Новое оборудование на серверах Vigrom",
				undername:"Как известно, политический процесс в современной России неравномерен. Типология средств..."
			},
			{
				id:"4",
				image:"image.svg",
				name:"Новое оборудование на серверах Vigrom",
				undername:"Как известно, политический процесс в современной России неравномерен. Типология средств..."
			},
			]
    }
  }
}
</script>

<style scoped>

.NewsWrappen{
width:1110px;
margin:auto;
}
.SelectedArticlesText{
margin-top:100px;
}
.SelectedArticlesTitle{
font-style: normal;
font-weight: 800;
font-size: 14px;
line-height: 19px;
text-transform:uppercase;
color: #FFFFFF;
}
.SelectedArticlesComp{
display:flex;
justify-content:space-between;
}
.NewsFeedText{
margin-top:100px;
}
.NewsFeedTitle{
font-style: normal;
font-weight: 800;
font-size: 14px;
line-height: 19px;
text-transform:uppercase;
color: #FFFFFF;
}
.foot{
margin-top:150px;	
}
</style>
