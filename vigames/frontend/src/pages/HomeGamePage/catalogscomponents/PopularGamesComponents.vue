<template>

	<div class="AllItem">
		<div class="ItemImage">

			<img v-bind:src="require('@/assets/img/' + Game_Popular.image) " width="1110" height="434">

		</div>
		<div class="Info">
			<div class="ItemInfoGame">
				<p class="NameGame1">{{Game_Popular.name}}

				</p>

				<p class="DiscriptionGame">{{Game_Popular.discription}}</p>
				<p class="LinkGame"><a href="#!" >Подробнее <img src="@/assets/img/strelka.svg" class="ImageArrow"></a></p>

			</div>
		</div>
	</div>

</template>

<script>


export default {
name: 'PopularGamesComponents',
components: {

},
props:{
	Game_Popular:{
		type:Object,
		default(){
			return{}
		}
	}
}


}
</script>

<style>
.AllItem{
position:relative;
 margin-top:48px;
}
.ItemImage{
	position:relative;
}

.Info{
	position:relative;
	width:1110px;;
	height:100px;
	top:-3px;
	background-color: #2D2D42;
}
.NameGame1{
	position: absolute;
	top: 35%;
    left: 4%;
	width:200px;
	color:#FFF;
	font-style: normal;
	font-weight: 800;
	font-size: 24px;
	line-height: 33px;
	text-transform:uppercase;
	padding-bottom:2px;
	height:28px;


}
.DiscriptionGame{
	position:absolute;
	top: 35%;
    left: 20%;
	width:470px;
	margin-left:30px;
	color:#fff;
	font-style: normal;
	font-weight: normal;
	font-size: 12px;
	line-height: 16px;
	padding-left:20px;
	border-left:1px solid #fff;

}
.LinkGame{
	position:absolute;
	top: 40%;
    left: 85%;


}
.LinkGame a{
	color:#fff;
	text-decoration:none;
	height:50px;
}
.ImageArrow{
	padding-left:10px;
}

</style>
