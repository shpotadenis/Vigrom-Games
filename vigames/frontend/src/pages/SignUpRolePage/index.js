const data = {

}

export default {
    name: "SignUpRolePage",
    data(){
        return{
            user: null,
            error: false
        }
    },
    methods:{
        check(){
            if (this.user) {
                this.$store.dispatch("user/changeRole", {
                    isDev: this.user == "dev"
                }).then(response => {
                    console.log(response)
                }).catch(e => {
                    console.log(e)
                })
                return true
            }
            this.error = true

        }
    },
    computed:{
        getGameData() {
            return data;
        }
    }
}