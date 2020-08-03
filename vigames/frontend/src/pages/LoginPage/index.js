const data = {

}

export default {
    name: "LoginPage",
    data() {
        return{
        nonEye: false,
        nonEyeconf: false,
        type: 'password',
        typeconf: 'password',
            confirmPass: null,
            pass: null,
            name: null,
            email: null,
            error_name: [],
            error_mail: [],
            error_pass: [],
            error_confirm: [],
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
        hideconf(){
            if (!this.nonEyeconf){
                this.nonEyeconf = true;
                this.typeconf = 'text';
            }
            else{
                this.nonEyeconf = false;
                this.typeconf = 'password';
            }
        },
        checkForm(e) {
            if (this.name && this.email && this.pass && this.confirmPass && (this.confirmPass==this.pass)) {
                return true;
            }
            this.error_name = []
                this.error_mail = []
                this.error_pass = []
                this.error_confirm = []

            if (!this.name) {
                this.error_name.push('Пустое поле');
            }
            if (!this.email) {
                this.error_mail.push('Пустое поле');
            }
            if (!this.pass) {
                this.error_pass.push('Пустое поле');
            }
            if (!this.confirmPass) {
                this.error_confirm.push('Пустое поле');
            } else{
                if (this.confirmPass!=this.pass){
                    this.error_confirm.push('Пароли не совпадают')
                }
            }
            this.errors++;
            e.preventDefault();
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