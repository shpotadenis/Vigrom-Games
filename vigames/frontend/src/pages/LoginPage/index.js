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
            error_confirm: []
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
                this.$store.dispatch('user/register', {
                    login: this.name,
                    password: this.pass,
                    email: this.email
                }).then(response => {
                    // Пользователь прошел первый этап регистрации, перенаправление ко второму
                      if (response) {
                        this.$router.push({
                            name: 'signUpRolePage'
                        })
                      }

                }).catch(e => {
                    if (e.username) { // Есть ошибки к полю имени
                        this.error_name = [...e.username] // Конкатенация массива error_name и username
                    }

                    if (e.email) {
                        this.error_mail = [...e.email]
                    }

                    if (e.password) {
                        this.error_pass = [...e.password]
                    }

                    this.errors++;
                })
            }

            this.error_name = []
            this.error_mail = []
            this.error_pass = []
            this.error_confirm = []

            if (!this.name) {
                this.error_name.push('Данное поле не заполнено');
            }
            if (!this.email) {
                this.error_mail.push('Данное поле не заполнено');
            }
            if (!this.pass) {
                this.error_pass.push('Данное поле не заполнено');
            }
            if (!this.confirmPass) {
                this.error_confirm.push('Данное поле не заполнено');
            } else{
                if (this.confirmPass!=this.pass){
                    this.error_confirm.push('Пароли не совпадают')
                }
            }
            e.preventDefault();
        }
    },
    components: {

    },
    computed: {
    },

    mounted() {
        // Пользователь уже авторизован -> редирект на ЛК
        if (this.$store.getters['user/isLoggedIn'] == true) {
            this.$router.push({
                name: 'personPage'
            })
        }

        // Пользователь ввел основные данные, но не выбрал роль
        if (this.$store.state.user.userLogin !== null && this.$store.state.user.isRoleSelected == false) {
            this.$router.push({
                name: 'signUpRolePage'
            })
        }
    }

}