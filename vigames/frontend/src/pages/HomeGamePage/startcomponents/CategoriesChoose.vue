<template>
<div class="TableCategories">
	<ul class="StartTable">
		<li class="Li">Жанры игр</li>
		<li class="Li">Платформа</li>
	</ul>
	<ul class="StartTable">
		<li class="Li">Жанры игр</li>
		<li class="Li">Платформа</li>
		<li class="Li">Платформа</li>
		<li class="Li">Платформа</li>
	</ul>
	<ul></ul>
	<ul></ul>
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
.TableCategories ul{
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

.StartTable .Li{
position:relative;
width:180px;
height:19px;
padding-left: 15px;
z-index:9999999999999999;
}


</style>
