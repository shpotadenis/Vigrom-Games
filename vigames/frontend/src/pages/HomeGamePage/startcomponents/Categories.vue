<template>
<div>
	<div class="AllCategories">
		<div class="CategoriesGame">
			<ul class="AllChooseUL">
				<li class="AllChooseLi" @click="toggleElement">Категории</li>
				<li class="AllChooseLi"><a href="#!">Скидки</a></li>
				<li class="AllChooseLi"><a href="#!">Бесплатные игры</a></li>
				<li class="AllChooseLi"><a href="#!">Ранний доступ</a></li>
			</ul>
		</div>
		<div class="FilterGames">
			<div class="SpaceBetweenImageAndText">
				<div class="SearchImage">
					<img src="@/assets/Search.svg">
				</div>
				<div class="SearchText">
					<input 
						type="text" 
						class="InputFilterGames" 
						placeholder="Начните вводить текст..." 
					>
				</div>
			</div>
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

import CategoriesChoose from "@/components/startcomponents/CategoriesChoose"

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
		CategoriesChoose
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
		margin-top:12px;
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
		background:#9E9E9E;
		margin-left:9px;
		border:none;
	}
	.InputFilterGames:active, :hover, :focus{
		outline:none;
	
	}
	.SpaceBetweenImageAndText{
		background-color:#9E9E9E;
	}
	.SearchImage{
		display:block;
		margin-top:9px;
		margin-left:9px;
	
	}
	input::placeholder{
		color: rgba(255, 255, 255, 0.3);

	}
	.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active до версии 2.1.8 */ {
  opacity: 0;
}
	
</style>