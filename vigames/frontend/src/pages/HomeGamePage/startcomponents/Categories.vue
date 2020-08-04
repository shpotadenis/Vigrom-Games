<template>
<div>
	<div class="AllCategories">
		<div class="CategoriesGame">
			<ul class="AllChooseUL">
				<li class="AllChooseLi" @click="toggleElement"><a href="#!">Категории <img src="@/assets/img/VectorBottom.svg"></a> </li>
				<li class="AllChooseLi"><a href="#!">Скидки</a></li>
				<li class="AllChooseLi"><a href="#!">Бесплатные игры</a></li>
				<li class="AllChooseLi"><a href="#!">Ранний доступ</a></li>
			</ul>
		</div>
		<div class="FilterGames">
			<search-component/>
		</div>
	</div>
   <transition name="fade">
		<categories-choose
			v-show="isVisible"
		/>
	</transition>
</div>
</template>

<script>

import CategoriesChoose from "./CategoriesChoose"
import SearchComponent from "@/components/SearchComponent/index.vue"

export default {
	name: 'Categories',
	data(){
		return{
			isVisible: false
		}
	},
	methods:{
		toggleElement(){
			this.isVisible = !this.isVisible
		}
	},
	components:{
		CategoriesChoose,
		SearchComponent
	}

}
</script>

<style>
	.AllCategories{
		widht:452px;
		display:flex;
		justify-content:space-between;
	}
	.CategoriesGame>ul{
		margin-top:15px;
	}
	.CategoriesGame>ul>li a{
		color: #7A7A83;
		text-decoration:none;

	}
	.AllChooseUL{
		display:flex;
	}
	.AllChooseLi{
		display:block;
		font-size: 14px;
		margin-right:30px;
		list-style:none;
		font-style: normal;
		font-weight: normal;
		line-height: 19px;
		color: #7A7A83;;
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
	.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

</style>
