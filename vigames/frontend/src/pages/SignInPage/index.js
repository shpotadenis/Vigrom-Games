const data = {

}

export default {
    name: "SignInPage",
    data() {
        return{
            nonEye: false,
            type: 'password'
        }
    },
    methods: {
        hide(){
            if (!this.nonEye){
                this.nonEye = true;
                this.type = 'text';
            }
            else{
                this.nonEye = false;
                this.type = 'password';
            }
        }
    },
    computed: {
        getGameData() {
            return data;
        }

    }

}