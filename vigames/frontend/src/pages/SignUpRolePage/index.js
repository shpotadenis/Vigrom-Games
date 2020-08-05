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
                    if (response) {
                        this.$router.push({
                            name: 'signInPage'
                        })
                    }
                }).catch(e => {
                    alert('Упс... Что-то пошло не так.')
                    console.log("Ошибка:")
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