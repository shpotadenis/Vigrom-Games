<template>
<div>
	<div class="AllCategories">
		<internal-menu
		/>
		<div class="FilterGames">
				<search-component/>
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
	data(){
		return{
			isVisible: false
		}
	},
	methods:{
		toggleElement(){
			this.isVisible = !this.isVisible
			}
		}
}
</script>

<style>
	.AllCategories{
		widht:452px;
		display:flex;
		justify-content:space-between;
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
