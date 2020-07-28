<template>
	<div class="wrappen">
		<news-section-page></news-section-page>
		<news-popular-page></news-popular-page>
		<news-feed-page></news-feed-page>
	</div>
</template>


<script>


	import NewsSectionPage from "@/components/Allcomponents/NewsSectionPage.vue"
	import NewsPopularPage from "@/components/Allcomponents/NewsPopularPage.vue"
	import NewsFeedPage from "@/components/Allcomponents/NewsFeedPage.vue"
	

	export default{
		name:"NewsPage",
		components:{
			NewsSectionPage,
			NewsPopularPage,
			NewsFeedPage
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
	position:relative;
	width:1000px;
	margin:0 auto;
	font-family:"Muller-Regular";
    src: url(../fonts/Muller-Regular.otf) format("woff");
	}
	
</style>