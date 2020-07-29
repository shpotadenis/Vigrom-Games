<template>
	<div class="wrappen">
		<div class="TopAll">
		<p class="TextNewsSection">Новостной раздел</p>
			<div class="SearchNewsSection">
				<div class="SearchBlock">
					<div class="ImgSearch">
						<img src="@/assets/img/search-icon.png">
					</div>
					<div class="InputSearch">
						<input type="text" placeholder="Поиск по новостям...">
					</div>
				</div>

			</div>
		</div>
		<div class="BlockNewsSection">
			<div class="BlockNewsSectionBackGr">
				<div class="AllinBlock">
					<div class="AboveTitle">СЕГОДНЯ</div>
					<div class="TitleAndUnderTitle">
						<div class="Title">Мы опускаем планку входа</div>
						<div class="UnderTitle">
							Унитарное государство, однако, доказывает системный политический процесс в современной России
						</div>
					</div>
					<div class="ButtonBlockNewsSection">
						<input class="Button" type="button" value="Подробнее">
						<img src="@/assets/img/Vector.png">
					</div>
				</div>
				<div class="BigImgWomen">
					<img src="@/assets/img/undraw_happy_news.png">
				</div>
			</div>
		</div>
	</div>
</template>


<script>


		

	export default{
		name:"NewsSectionPage",
		components:[{

		}],
		props:{},
		data(){
			return{

			}
		},
		methods:{
	
		}
	}
</script>

<style scoped>
	.TextNewsSection{
		font-family: 'Muller-Bold';
		font-style: normal;
		font-weight:800;
		font-size: 18px;
		line-height: 14px;
		float:left;
	}
	.TopAll{
		display:flex;
		justify-content: space-between;
	}
	.SearchNewsSection{
		padding-top:6px;
	}
	.SearchBlock{
		display:flex;
		padding-left:15px;
	}
	.InputSearch{
		padding-left:12px;

	}
	input[type=text]{
		border:none;
	}
	input[type=text]:active, :hover, :focus {
    outline: 0;
    outline-offset: 0;
}
	.BottomLine{
		position:relative;
		height:12px;
		top:-6px;

	}
	.BlockNewsSectionBackGr{
		position:relative;
		height: 294px;
		background-color:#F9F9F9;
		top:30px;
	}
	.AllinBlock{
		position:absolute;
		left:40px;
		top:40px;
	}
	.AboveTitle{
		font-style: normal;
		font-weight: normal;
		font-size: 14px;
		line-height: 14px;
		color: #7A7A83;
	}
	.TitleAndUnderTitle{
		position:relative;
		top:64px;
		
	}
	.Title{
		font-style: normal;
		font-weight: 800;
		font-size: 24px;
		line-height: 24px;
		color:#000000;
	}
	.UnderTitle{
		font-style: normal;
		font-weight: normal;
		font-size: 14px;
		margin-top:10px;
		line-height: 14px;
		color: #7A7A83;

	}
	.ButtonBlockNewsSection{
		position:relative;
		top:90px;
		width:139px;
		display:flex;
		
	}
	.Button{
		width: 139px;
		height: 38px;
		background: #CE6796;
		border:none;
		color:#ffffff;
		text-indent:-30px;
	}
	.BigImgWomen{
		position:relative;
		top:20px;
		float:right;
	}


</style>