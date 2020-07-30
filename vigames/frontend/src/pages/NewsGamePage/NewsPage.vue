<template>
	<div class="wrappen">
		<news-section-page></news-section-page>
		<news-popular-page></news-popular-page>
		<news-feed-page></news-feed-page>
		<footer-component></footer-component>
	</div>
</template>


<script>


	import NewsSectionPage from "./Allcomponents/NewsSectionPage.vue"
	import NewsPopularPage from "./Allcomponents/NewsPopularPage.vue"
	import NewsFeedPage from "./Allcomponents/NewsFeedPage.vue"
	import FooterComponent from "../../components/FooterComponent/index.vue"
	

	export default{
		name:"NewsPage",
		components:{
			NewsSectionPage,
			NewsPopularPage,
			NewsFeedPage,
			FooterComponent
		},
		props:{},
		data(){
			return{

			}
		}
	}
</script>

<style scoped>
	.wrappen{
	width:1000px;
	margin:0 auto;
	font-family:"Muller-Regular";
    /*src: url(../fonts/Muller-Regular.otf) format("woff");*/
	}
	
</style>