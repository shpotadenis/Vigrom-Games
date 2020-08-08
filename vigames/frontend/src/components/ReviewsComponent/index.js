import games from '../../api/modules/games.js'
export default {
    name: "ReviewsComponent",
    data() {
        return {
            reviewFormShow: false,
            content: '',
            rating: 1,
            loading: false,
            reviews: ''
        }
    },
    props: ['gameData'],
    beforeMount() {
      this.fetchData()
    },
    methods: {
        sendBtnClick() {
            this.$store.dispatch('user/addReview', {
                gameId: this.gameData.id,
                mark: this.rating,
                comment: this.content
            }).then(response => {
                this.$emit('update-game')
                this.reviewFormShow = false
                console.log(response)
            }).catch(error => {
                console.log(error)
            })
        },

        fetchData() {
            this.loading = true
            games.getReviews(this.gameData.id).then(response => {
                this.loading = false
                this.reviews = response.data
            }).catch(error => {
                console.log(error)
            })
            this.loading = false
        }
    }
}