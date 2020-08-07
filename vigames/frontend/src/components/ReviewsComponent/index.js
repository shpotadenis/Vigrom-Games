const reviews = [
    {
        id: 1,
        user_nickname: 'Name',
        title: 'Мой первый отзыв',
        rating: 3,
        text: 'Maecenas nec nunc lectus. Phasellus suscipit dui id rhoncus iaculis. Proin lobortis, enim nec condimentum vulputate, augue risus fermentum purus, ac pharetra orci justo nec tellus. Ut augue ex, laoreet in orci et, eleifend volutpat augue. Donec tempor dignissim diam blandit viverra. Praesent et neque blandit, ornare arcu imperdiet, tincidunt magna. Etiam sed fermentum lectus, vitae porta mauris. Proin pharetra enim eget enim facilisis, in facilisis enim tincidunt.'
    }
]


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
            this.reviews = reviews
            this.loading = false
        }
    }
}