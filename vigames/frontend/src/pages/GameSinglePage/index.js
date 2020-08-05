import ReviewsComponent from "../../components/ReviewsComponent/index.vue";
import BreadcrumbsComponent from "../../components/BreadcrumbsComponent/index.vue"
import FooterComponent from "../../components/FooterComponent/index.vue"
import Checkout from "../../components/Pop-ups/Checkout/checkout"
import SliderComponent from './SliderComponent/SliderComponent.vue'

export default {
    name: "GameSinglePage",
    components: {
        ReviewsComponent,
        BreadcrumbsComponent,
        FooterComponent,
        Checkout,
        SliderComponent
    },
    data() {
        return {
            isBtnClick: false,
            loading: true
        }
    },

    computed: {
        getGameData() {
            return this.$store.getters['games/getGame'](this.$route.params.id)
        },

        getImages() {
            let images = []
            for (let i in this.getGameData.image) {
                images.push({
                    image: this.getGameData.image[i].img
                })
            }
            return images
        },

        breadcrumbs() {
            return [
                {
                    to: {
                        name: 'homePage'
                    },
                    title: 'Главная'
                },
                {
                    title: this.getGameData.title
                }
            ]
        },
    },

    // eslint-disable-next-line no-unused-vars
    beforeRouteUpdate(to, from, next) {
        this.fetchData(to.params.id)
        next()
    },

    mounted() {
      this.fetchData(this.$route.params.id)
    },

    methods: {
        fetchData(gameId) {
            this.loading = true
            this.$store.dispatch('games/loadGame', {
                id: gameId
            }).then(response => {
                this.loading = false
                // FIXME: Убрать отладочный вывод
                console.log('GameAdded:')
                console.log(response)
            }).catch(error => {
                // TODO: Убрать отладочный вывод, редирект на 404
                console.log("Ошибка в GSP")
                console.log(error)
            })
        }
    }

}
