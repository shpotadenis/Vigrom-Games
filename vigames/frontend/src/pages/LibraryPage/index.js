import FooterComponent from '../../components/FooterComponent/index.vue'
import SearchComponent from '../../components/SearchComponent/index.vue'
import ContentCardComponent from '../../components/ContentCardComponent/index.vue'
import GameCard from "@/components/GameCard/GameCard.vue"
import { convertApiToComponentObj } from '../../utils.js'

export default {
    name: 'LibraryPage',
    components: {
        FooterComponent,
        SearchComponent,
        ContentCardComponent,
        GameCard
    },
    data() {
        return {
            loading: true,
        }
    },

    mounted() {
        this.fetchData()
    },

    computed: {
        getLibraryCards() {
            let libraryCards = this.$store.getters['user/getLibrary'] // Карточки, полученные из API
            let libraryComponentCards = [] // Сконвертированные карточки для компонента GameCard
            for (let i in libraryCards) {
                libraryComponentCards.push(convertApiToComponentObj(libraryCards[i]))
            }
            return libraryComponentCards
        }
    },
    methods: {
        fetchData() {
            this.$store.dispatch('user/getLibrary').then(response => {
                this.loading = false;
                console.log('Library added:')
                console.log(response)
            }).catch(error => {
                console.log('Library error')
                console.log(error.response)
            })
        },


    }
}
