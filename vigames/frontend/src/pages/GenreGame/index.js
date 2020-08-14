import InternalMenu from '../../components/InternalMenu/InternalMenu.vue'
import SearchComponent from '../../components/SearchComponent/index.vue'
import GameCard from  '../../components/GameCard/GameCard.vue'
import FooterComponent from '../../components/FooterComponent/index.vue'
import games from '../../api/modules/games.js'
import {convertApiToComponentObj} from "../../utils";

export default{

    name:"GenreGame",
    components:{
        InternalMenu,
        SearchComponent,
        GameCard,
        FooterComponent
    },

    data(){
        return{
            discountgames:[],
            loading: false
        }
    },

    // eslint-disable-next-line no-unused-vars
    beforeRouteUpdate(to, from, next) {
        this.fetchData(to.params.genre)
        next()
    },
    beforeMount() {
      this.fetchData(this.$route.params.genre)
    },
    computed: {
        array() {
            return this.discountgames.slice(0, 8)
        },
        array2() {
            return this.discountgames.slice(8)
        }
    },

    methods: {
        fetchData(genre) {
            this.loading = true;
            games.getByGenre(genre).then(response => {
                for (let i in response.data) {
                    response.data[i] = convertApiToComponentObj(response.data[i])
                }
                this.discountgames = response.data
                this.loading = false
            }).catch(error => {
                console.log(error)
            })
        },
        getGenreName() {
            let genres = [
                {name: 'Приключения', value: 'adventures'},
                {name: 'Головоломки', value: 'puzzles'},
                {name: 'Экшн', value: 'action'},
                {name: 'РПГ', value: 'rpg'},
                {name: 'Стратегии', value: 'strategy'},
                {name: 'Фермы', value: 'farms'},
                {name: 'ММО', value: 'mmo'},
                {name: 'Шутеры', value: 'shooters'},
                {name: 'Гонки', value: 'race'},
                {name: 'Симуляторы', value: 'simulators'}
            ];
            return genres.filter(g => g.value == this.$route.params.genre)[0].name
        }
    }
}
