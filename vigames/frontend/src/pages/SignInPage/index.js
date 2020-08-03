const data = {

}

export default {
    name: "SignInPage",
    data() {
        return{
            nonEye: false,
            type: 'password',
            pass: null,
            name: null,
            error_name: [],
            error_pass: [],
            errors: 0
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
        checkForm(e) {
            if (this.name && this.pass) {
                return true;
            }
            this.error_name = []
            this.error_pass = []

            if (!this.name) {
                this.error_name.push('Пустое поле');
            }
            if (!this.pass) {
                this.error_pass.push('Пустое поле');
            }
            this.errors++;
            e.preventDefault();
        }
    },
    computed: {
        getGameData() {
            return data;
        }

    }

}