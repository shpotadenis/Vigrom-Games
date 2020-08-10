import InternalMenu from '../../components/InternalMenu/InternalMenu.vue'
import SearchComponent from '../../components/SearchComponent/index.vue'
import GameCard from  '../../components/GameCard/GameCard.vue'
import BannerComponent from  '../../components/BannerComponent/index.vue'
import FooterComponent from '../../components/FooterComponent/index.vue'
import games from '../../api/modules/games.js'

export default{

    name:"GenreGame",
    components:{
        InternalMenu,
        SearchComponent,
        GameCard,
        BannerComponent,
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
        this.fetchData()
    },
    beforeMount() {
      this.fetchData()
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
        fetchData() {
            this.loading = true;
            games.getByGenre(this.$route.params.genre).then(response => {
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
