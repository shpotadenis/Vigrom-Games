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
            breadcrumbs: [
                {
                    to: {
                        name: 'homePage'
                    },
                    title: 'Главная'
                }
            ]
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
    },

    // eslint-disable-next-line no-unused-vars
    beforeRouteUpdate(to, from, next) {
        this.fetchData()
        next()
    },

    created() {
        this.fetchData()
    },

    methods: {
        fetchData() {
            if (this.$route.params.id) {
                this.$store.dispatch('games/loadGame', {
                    id: this.$route.params.id
                }).then(response => {
                    this.breadcrumbs.push({
                        title: this.getGameData.title
                    })
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

}
