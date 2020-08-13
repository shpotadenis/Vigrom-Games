<template>

	<div class="AllItem">
		<div class="ItemImage">

			<img v-bind:src="getImage" width="1110" height="434">

		</div>
		<div class="Info">
			<div class="ItemInfoGame">
				<p class="NameGame1">{{Game_Popular.title}}

				</p>

				<p class="DiscriptionGame">{{Game_Popular.short_description}}</p>
				<p class="LinkGame"><router-link :to="{name: 'singlePage', params: { id: Game_Popular.id }}" >Подробнее <img src="@/assets/img/strelka.svg" class="ImageArrow"></router-link></p>

			</div>
		</div>
	</div>

</template>

<script src="./PopularGamesComponents.js">
</script>

<style lang='scss'>
@import '@/assets/style/PopularGamesComponents.scss'
</style>
