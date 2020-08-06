import FooterComponent from '../../components/FooterComponent/index.vue'
import SearchComponent from '../../components/SearchComponent/index.vue'
import BannerComponent from '../../components/BannerComponent/index.vue'
import ContentCardComponent from '../../components/ContentCardComponent/index.vue'
import GameCard from "@/components/GameCard/GameCard.vue"

export default {
    name: 'LibraryPage',
    components: {
        FooterComponent,
        SearchComponent,
        BannerComponent,
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
                libraryComponentCards.push(this.convertApiToComponentObj(libraryCards[i]))
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

        convertApiToComponentObj(object) {
            let obj = {
                id: object.id,
                name: object.title,
                undername: object.author,
                image: object.img,
                icon: '',
                price: object.price
            }

            if (object.image[0]) {
                obj.scrin = object.image[0].img
            }

            if (object.image[1]) {
                obj.scrin1 = object.image[1].img
            }

            if (object.image[2]) {
                obj.scrin2 = object.image[2].img
            }

            if (object.image[3]) {
                obj.scrin3 = object.image[3].img
            }

            return obj
        }
    }
}
