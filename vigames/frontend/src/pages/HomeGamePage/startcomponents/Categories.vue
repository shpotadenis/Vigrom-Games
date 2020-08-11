<template>
<div container>
	<div class="AllCategories row justify-content-between">

		<div class="col-6">
			<internal-menu/>
		</div>
		<div class="FilterGames col-4">
<<<<<<< HEAD
				<search-component searchzone="games"/>
=======
				<search-component key="game"/>
>>>>>>> d406618dc2755c3f420993429adae26fff763fe0
		</div>
	</div>

</div>
</template>

<script>

import SearchComponent from "@/components/SearchComponent/index.vue"
import InternalMenu from "@/components/InternalMenu/InternalMenu.vue"


export default {
	name: 'Categories',
	components:{
		SearchComponent,
		InternalMenu
	},
}
</script>

<style>
	.AllChooseUL{
		display:flex;
	}
	.AllChooseLi{
		display:block;
		cursor: pointer;
		text-decoration: none;
		font-size: 14px;
		margin-right:30px;
		list-style:none;
		font-style: normal;
		font-weight: normal;
		line-height: 19px;
		color: #7A7A83;
	}

	.FilterGames{
		margin-top:5px;
		margin-bottom:5px;
	}
	.SpaceBetweenImageAndText{
		display:flex;
	}
	.InputFilterGames{
		width: 300px;
		height: 33px;
		background:#212130;
		margin-left:9px;
		border:none;
	}
	.InputFilterGames:active, :hover, :focus{
		outline:none;

	}
	.SpaceBetweenImageAndText{
		background-color:#212130;
		margin-left:20px;
	}
	.SearchImage{
		display:block;
		margin-top:0px;
		margin-right:10px;

	}
	input[type=text]{
		color:#fff;
	}
	.BorderTop{
	position:relative;
	top:7px;
		width:350px;
		height:1px;
		background: #7A7A83;
	}
	input::placeholder{
		color: rgba(255, 255, 255, 0.3);

	}


</style>
