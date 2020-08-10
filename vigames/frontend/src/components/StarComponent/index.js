export default {
    name: "StarComponent",
    data() {
      return {
          rating: 0
      }
    },
    methods: {
        ratingClick(i) {
            this.rating = i
            this.$emit('rating-select', i)
        },
        getFilledStatus(i) {
            if (i > this.rating) {
                return ''
            } else {
                return '-filled'
            }
        }
    },
    computed: {

    }
}