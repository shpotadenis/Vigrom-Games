import {getImageUrl} from "../../../utils";

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
},
	computed: {
		getImage() {
			return getImageUrl(this.Game_Popular.banner)
		}
	}



}
