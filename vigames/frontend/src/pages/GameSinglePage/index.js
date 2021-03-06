import ReviewsComponent from "../../components/ReviewsComponent/index.vue";
import BreadcrumbsComponent from "../../components/BreadcrumbsComponent/index.vue"
import FooterComponent from "../../components/FooterComponent/index.vue"
import Checkout from "../../components/Pop-ups/Checkout/checkout"
import SliderComponent from './SliderComponent/SliderComponent.vue'
import user from '../../api/modules/user.js'
import { getImageUrl } from '../../utils.js'
// eslint-disable-next-line no-unused-vars
import games from "../../api/modules/games";

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
            loading: false,
            gameData: null
        }
    },

    computed: {
        getGameData() {
            return this.gameData
        },

        isPurchased() {
          return this.$store.getters['user/isGamePurchased'](this.$route.params.id)
        },

        isInWishlist() {
          return this.$store.getters['user/isInWishlist'](this.$route.params.id)
        },

        getImages() {
            let images = []
            for (let i in this.getGameData.image) {
                images.push({
                    image: getImageUrl(this.getGameData.image[i].img)
                })
            }
            return images
        },
        getGenre() {
            let genres = [{name: 'Приключения', value: 'adventures'},
            {name: 'Головоломки', value: 'puzzles'},
            {name: 'Экшн', value: 'action'},
            {name: 'РПГ', value: 'rpg'},
            {name: 'Стратегии', value: 'strategy'},
            {name: 'Фермы', value: 'farms'},
            {name: 'ММО', value: 'mmo'},
            {name: 'Шутеры', value: 'shooters'},
            {name: 'Гонки', value: 'race'},
            {name: 'Симуляторы', value: 'simulators'}]
            return genres.filter(g => g.value == this.getGameData.genre)[0].name
        },

        getCheckoutGameData() {
            return {
                id: this.getGameData.id,
                name: this.getGameData.title,
                price: this.getGameData.price
            }
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

    beforeMount() {
      this.fetchData(this.$route.params.id)
    },

    methods: {
        fetchData(gameId) {
            this.loading = true
             games.getGameInfo(gameId).then(response => {
                if (response.data) {
                    this.gameData = response.data
                    this.gameData.id = gameId
                }
                this.loading = false
            }).catch(error => {
                console.log(error)
                this.$router.push({
                    name: 'errorPage404'
                })
            })
        },
        downloadBtnClick() {
            user.downloadGame(this.$route.params.id).then(response => {
                console.log(response)
                const url = window.URL.createObjectURL(new Blob([response.data]))
                const link = document.createElement('a')
                link.href = url
                link.setAttribute('download', this.getGameData.title + '.zip') //or any other extension
                document.body.appendChild(link)
                link.click()
            }).catch(error => {
                console.log(error.response)
            })
        },
        updateGame() {
            this.fetchData(this.$route.params.id)
            this.$scrollTo('#reviews', 100)
        },

        addToWishlistClick() { //is_hidden
            this.$store.dispatch('user/addToWishlist', {
                gameId: this.$route.params.id
            }).catch(error => {
                console.log('Error "addToWishlistClick"')
                console.log(error)
            })
        },

        removeFromWishlistClick() {
            this.$store.dispatch('user/removeFromWishlist', {
                gameId: this.$route.params.id
            }).catch(error => {
                console.log('Error "removeFromWishlist"')
                console.log(error)
            })
        }
    }

}
