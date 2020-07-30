<template>
<div class="container">
	<div class="col">
		<div class="wrappen">
			<footer-component></footer-component>
		</div>
	</div>
</div>
</template>


<script>



	import FooterComponent from "../../components/FooterComponent/index.vue"


	export default{
		name:"NewsPage",
		components:{

			FooterComponent
		},
		props:{},
		data(){
			return{

			}
		}
	}
</script>

<style scoped>
.wrappen{
	width:1100px;
	margin:0 auto;
}

</style>
