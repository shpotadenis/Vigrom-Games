const data = {
    donate1: 0,
    donate2: 100,
    donate3: 200
}

export default {
    name: "checkout",
    components: {},
    data() {
        return {

        }
    },
    methods: {
        closeCheckout () {
            this.$emit( event: 'closeCheckout')
        },


    }
}
