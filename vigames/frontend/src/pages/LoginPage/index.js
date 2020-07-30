const data = {

}

export default {
    name: "LoginPage",
    data() {
        return{
        nonEye: false,
            nonEyeconf: false,
        type: 'password',
            typeconf: 'password'
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
        },
        hideconf(){
            if (!this.nonEyeconf){
                this.nonEyeconf = true;
                this.typeconf = 'text';
            }
            else{
                this.nonEyeconf = false;
                this.typeconf = 'password';
            }
        }
    },
    components: {

    },
    computed: {
        getGameData() {
            return data;
        }

    }

}