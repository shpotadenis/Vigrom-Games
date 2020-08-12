import StarComponent from '../StarComponent/index.vue'
import { getImageUrl } from "../../utils";

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
    computed: {
      canReview() {
          return this.$store.getters['user/isLoggedIn'] && !this.reviews.some(i => i.author == this.$store.getters['user/getUserName']);
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
        getImage(i) {
            return getImageUrl(this.reviews[i].avatar)
        },
        selectedRating(i) {
            this.rating = i
        }
    }
}