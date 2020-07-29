<template>
	<div class="wrappen">
		<div class="FilterAndTitle">
			<p class="TextNewsFeed">Новостная лента</p>
			<input type="text" placeholder="Фильтры">
		</div>
		<div class="NewsFeedPageComponents">
			<news-feed-page-components
				v-for="item1 in items1"
				:key="item1.article"
				v-bind:News_feed="item1"
			/>
		</div>
		
	</div>
</template>

<script>
	
	import NewsFeedPageComponents from "./NewsFeedPageComponents"
	export default{
		name:"NewsFeedPage",
		components:{
			NewsFeedPageComponents
		},
		props:{},
		data() {
			return{
				items1:[
					{
						undertitle:'Как известно, политический процесс в современной России неравномерен.',
						image:"image.png",
						title:" Vigrom",
						arcticle:"T1"
					},
					{
						undertitle:'Как известно, политический процесс в современной России неравномерен. Типология средств...',
						image:"image.png",
						title:"Новое оборудование на серверах Vigrom",
						arcticle:"T2"
					},
					{
						undertitle:'Как известно, политический процесс в современной России неравномерен.',
						image:"image.png",
						title:" Vigrom",
						arcticle:"T3"
					},
					{
						undertitle:'Как известно, политический процесс в современной России неравномерен. Типология средств...',
						image:"image.png",
						title:"Новое оборудование на серверах Vigrom",
						arcticle:"T4"
					}
				]
			}
		}
	}
</script>

<style scope>
	.NewsFeedPageComponents{
		top:430px;
		display:flex;
		flex-wrap:wrap;
		justify-content:space-between;
	}
	.FilterAndTitle{
		top:380px;
		width:900px;
		display:flex;
		justify-content:space-between;
	}
	input[type=text]{
		border:none;
	}
	input[type=text]:active, :hover, :focus{
		outline:0;
		outline-offset:0;
	}
	
    
	.TextNewsFeed{
		font-family: 'Muller-Bold';
		font-style: normal;
		font-weight:800;
		font-size: 18px;
		line-height: 14px;
		margin:0px;
		float:left;
	}

</style>


