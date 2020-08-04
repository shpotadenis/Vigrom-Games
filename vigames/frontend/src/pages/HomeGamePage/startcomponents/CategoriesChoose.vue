<template>
<div class="TableCategories">
	<ul class="StartTable">
		<li>Жанры игр
			<ul>
				<li class="LiGenre">Приключения</li>
				<li class="LiGenre">Головоломки</li>
				<li class="LiGenre">Экшн</li>
				<li class="LiGenre">РПГ</li>
			</ul>
		</li>
		<li class="a1">a
			<ul>
				<li class="LiGenre">Стратегии</li>
				<li class="LiGenre">Фермы</li>
				<li class="LiGenre">ММО</li>
				<li class="LiGenre">Шутеры</li>
			</ul>
		</li>
		<li class="v1">v
			<ul>
				<li class="LiGenre">Гонки</li>
				<li class="LiGenre">Симуляторы</li>
			</ul>
		</li>
		<li>Платформа
		<ul>
			<li class="LiGenre">Windows</li>
			<li class="LiGenre">MacOS</li>
		</ul>
		</li>
	</ul>
</div>
</template>

<script>



export default {
  name: 'CategoriesChoose',
  props:{

		},
		data(){
			return{

			}
		},
  components: {

  }
}
</script>

<style>
.TableCategories{
	position:absolute;
	display:flex;
	justify-content:space-between;
	background: #2D2D42;
	border-radius: 10px;
	width:720px;
	height:155px;
	color:#fff;
	z-index: 999999;
}
.StartTable {
	width:720px;
display:flex;
justify-content:space-between;
}
.StartTable li{
width:180px;
height:29px;
padding-top:10px;
padding-left: 15px;
z-index:9999999999999999;
}
.StartTable>li>ul>li{
width:180px;
height:19px;
padding-top:10px;
padding-left:0;
z-index:9999999999999999;
font-style: normal;
font-weight: normal;
font-size: 14px;
line-height: 19px;
color: #7A7A83;
}
.LiGenre{
margin-top:8px;
}
.LiGenre1{
margin-top:8px;
}
.v1{
content:'';
color: #2D2D42;
}
.a1{
content:'';
color: #2D2D42;
}
</style>
