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

<script src="./PopularGamesComponents.js">
</script>

<style lang='scss'>
@import '@/assets/style/PopularGamesComponents.scss'
</style>
