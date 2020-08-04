<template>
<div class="TableCategories">
	<ul class="StartTable">
		<li>Жанры игр</li>
		<li>Платформа</li>
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
height:19px;
padding-top:10px;
padding-left: 15px;
z-index:9999999999999999;
}


</style>
