<template>
	<div class="wrappen">
		<a href="#!" class="LinkFeedNews">
		<div class="BlockFeedNews">

			<img class="ImageFeed" src="src/assets/img/pic1.png" alt="img" width="430" height="258">

			<p class="TitleFeed">
				{{News_feed.title}}
			</p>
			<p class="UnderTitleFeedNews">
				{{News_feed.undertitle}}
			</p>	
		</div>
	</a>
		
	</div>
</template>

<script>

	export default{
		name:"NewsFeedPageComponents",
		components:{
			
		},
		props:{
			News_feed:{
				type:Object,
				default(){
					return{}
				}
			}
		},
		data() {
			return{
		
			}
		}
	}
</script>

<style scope>
	.LinkFeedNews{
		color:#000;
		text-decoration: none;
	}
	.BlockFeedNews{
		width:430px;
		height:258px;
		margin-bottom:136px;
	}
	.TitleFeed{
		width: 387px;
		height: 5px;
		font-size:14px;
		font-style: normal;
		font-weight: bold;
		font-size: 18px;
		text-decoration: none;
	}
	.UnderTitleFeedNews{
		width: 430px;
		height: 38px;
		text-align:left;
		font-style: normal;
		font-weight: normal;
		font-size: 14px;
		line-height: 19px;
		color: #ADADAD;
		text-decoration: none;
		
	}
	ImageFeed{
		
	}


</style>