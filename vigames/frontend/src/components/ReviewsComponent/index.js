// eslint-disable-next-line no-unused-vars
import games from '../../api/modules/games.js'
import StarComponent from '../StarComponent/index.vue'

export default {
    name: "ReviewsComponent",
    components: {
      StarComponent
    },
    data() {
        return {
            reviewFormShow: false,
            content: '',
            rating: null,
            title: null,
            loading: false,
        }
    },
    props: ['reviews', 'gameData'],
    methods: {
        sendBtnClick() {
            this.$store.dispatch('user/addReview', {
                gameId: this.gameData.id,
                mark: this.rating,
                comment: this.content,
                title: this.title
            }).then(response => {
                this.$emit('update-game')
                this.reviewFormShow = false
                console.log(response)
            }).catch(error => {
                console.log(error)
            })
        },
        selectedRating(i) {
            this.rating = i
            console.log(i)
        }
       /* fetchData() {
            this.loading = true
            games.getReviews(this.gameData.id).then(response => {
                this.reviews = response.data
                console.log(response)
                this.loading = false
            }).catch(error => {
                console.log(error)
            })
        }, */
    }
}