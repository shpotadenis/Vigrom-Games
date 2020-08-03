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
            if (this.user){
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