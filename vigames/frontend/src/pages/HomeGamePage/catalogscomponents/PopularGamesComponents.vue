<template>
<div id="wrappen">
	<div class="AllItem">
		<div class="ItemImage">
			<img src="@/assets/img/pic1.png" width="1000" height="390">
		</div>
		<div class="Info">
			<div class="ItemInfoGame">
				<p class="NameGame">NameGame</p>
				<p class="DiscriptionGame">Мультиплатформенная компьютерная игра в жанре action/RPG, разработанная
польской студией CD Projekt RED</p>
	
			</div>
			
				
		</div>
	</div>
</div>
</template>

<script>


export default {
  name: 'PopularGamesComponents',
  components: {
    
  }
}
</script>

<style>
.AllItem{
position:relative;
 margin-top:48px;
}
.Info{
	position:relative;
	width:1000px;;
	height:90px;
	top:-3px;
	background-color: #2D2D42;
}
.NameGame{
	color:#FFF;
	font-style: normal;
	font-weight: 800;
	font-size: 24px;
	line-height: 33px;
	text-transform:uppercase;
	position: absolute;
	padding-bottom:2px;
	padding-right:40px;
	height:28px;
    top: 35%;
    left: 4%;
    border-right:1px solid #fff;
}
.DiscriptionGame{
	position:absolute;
	top: 30%;
    left: 27%;
	width:470px;
	color:#fff;
	font-style: normal;
	font-weight: normal;
	font-size: 12px;
	line-height: 16px;

}

</style>