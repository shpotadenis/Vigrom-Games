import games from '../../api/modules/games.js'
export default {
    name: "ReviewsComponent",
    data() {
        return {
            reviewFormShow: false,
            content: '',
            rating: null,
            title: null,
            loading: false,
            reviews: [],
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

        fetchData() {
            this.loading = true
            games.getReviews(this.gameData.id).then(response => {
                this.reviews.push(response.data)
                console.log(response)
                this.loading = false
            }).catch(error => {
                console.log(error)
            })
        },
    }
}