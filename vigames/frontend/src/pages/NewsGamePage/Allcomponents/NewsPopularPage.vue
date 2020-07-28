<template>
	<div class="wrappen">
	<p class="TextNewsPopular">Популярные статьи</p>
		<div class="TopAllPopular">
			<news-popular-page-components
				v-for="item in items"
				:key="item.arcticle"
				v-bind:News_data="item"
			/>
		</div>
		
	</div>
</template>

<script>

	import NewsPopularPageComponents from "@/components/Allcomponents/NewsPopularPageComponents"

	export default{
		name:"NewsPopularPage",
		components:{
			NewsPopularPageComponents
		},
		props:{},
		data() {
			return{
				items:[
					{
						date: "СЕГОДНЯ",
						image: "image.png",
						title: "Новое оборудование на серверах Vigrom",
						arcticle: "T1",
						available: true
					},
					{
						date: "ВЧЕРА",
						image: "Rectangle.png",
						title: "Конкурс на лучший проект площадки",
						arcticle: "T2",
						available: true
					},
					{
						date: "СЕГОДНЯ",
						image: "undraw.svg",
						title: "Новое оборудование на серверах Vigrom",
						arcticle: "T3",
						available: true
					},
					{
						date: "ВЧЕРА",
						image: "image.png",
						title: "Конкурс на лучший проект площадки",
						arcticle: "T4",
						available: true
					}
				]
			}
		}
	}
</script>

<style scope>
	.TopAllPopular{
		position:absolute;
		top:145px;
		width:800px;
		display:flex;
		justify-content:space-between;
		align-item:center;
	}
	.TextNewsPopular{
		position:absolute;
		top:100px;
		width:900px;
		font-family: 'Muller-Bold';
		font-style: normal;
		font-weight:800;
		font-size: 18px;
		line-height: 14px;
		margin:0px;
		float:left;
	}

</style>


