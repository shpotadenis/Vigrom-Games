<template>
	<div>
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

			</div>
			</div>
	</div>
</div>
		<footer-component></footer-component>
	</div>
</template>


<script src="./NewsPage.js">
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
