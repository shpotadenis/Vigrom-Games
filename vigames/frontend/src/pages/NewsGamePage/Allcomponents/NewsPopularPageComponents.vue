<template>
<div>
	<a href="#!" class="LinkPopularNews">
		<div class="BlockPopularNews">
			<p class="Date">{{News_data.date}}</p>
			<img class="Image" v-bind:src=" require('@/assets/' + News_data.image) " alt="img" width="200" height="200">
			<p class="TitlePopularNews">{{News_data.title}}</p>	
		</div>
	</a>
</div>	
</template>

<script>

	export default{
		name:"NewsPopularPageComponents",
		components:[{

		}],
		props:{
			News_data:{
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

	}
</script>

<style scope>
	.LinkPopularNews{
		color:#000;
	}
	.BlockPopularNews{
		position:absolute;
		width:200px;
		height:200px;
	}
	.Date{
		position:absolute;
		top:10px;
		left:30px;
		z-index:100;
		font-size:14px;
	}
	.TitlePopularNews{
		position:absolute;
		text-align:left;
		font-size:18px;
		font-weight:bold;
		left:30px;
		top:100px;
		width: 160px;
		height: 75px;
	}
	Image{
		position:absolute;
	}


</style>
