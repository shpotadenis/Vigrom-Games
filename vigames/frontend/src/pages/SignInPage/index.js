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
            errorMessage: ''
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
                this.$store.dispatch('user/login', {
                    login: this.name,
                    password: this.pass
                }).then(response => {
                    if (response) {
                        this.$router.push({
                            name: 'personPage'
                        })
                    }
                }).catch(error => {
                    if (error.non_field_errors) {
                        this.errorMessage = error.non_field_errors[0]
                    }
                })

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
            e.preventDefault();
        }
    },
    computed: {
    },
    mounted() {
        if (this.$store.getters['user/isLoggedIn'] == true) {
            this.$router.push({
                name: 'personPage'
            })
        }
    }

}