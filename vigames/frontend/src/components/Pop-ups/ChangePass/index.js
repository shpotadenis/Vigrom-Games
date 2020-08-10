import PasswordChanged from '../PasswordChanged/index.vue'

export default {
    name: "v_popup",
    props: {
    },
    components: {
      PasswordChanged
    },
    data() {
        return {
            type: 'password',
            typeconf: 'password',
            typeconf_repeat: 'password',
            nonEye: false,
            nonEyeconf: false,
            nonEyeconf_repeat: false,
            old_pass: null,
            new_pass: null,
            new_pass_repeat: null,
            allgood: false,
            error_old_pass: [],
            error_new_pass: [],
            error_new_pass_repeat: [],
            errors: 0,
            isPassChangedPopupVisible: false
        }
    },
    methods: {
        closePopup() {
            this.$emit('closePopup')
        },
        SaveNewPass() {
            if (this.allgood == true){
                this.$emit('SaveNewPass')
            }
        },
        close() {
            this.closePopup()
        },
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
        hideconf_repeat(){
            if (!this.nonEyeconf_repeat){
                this.nonEyeconf_repeat = true;
                this.typeconf_repeat = 'text';
            }
            else{
                this.nonEyeconf_repeat = false;
                this.typeconf_repeat = 'password';
            }
        },
        checkForm(e) {
            if (this.old_pass && this.new_pass && this.new_pass_repeat && (this.new_pass_repeat==this.new_pass)) {
                this.$store.dispatch('user/changePassword', {
                    new_password: this.new_pass,
                    current_password: this.old_pass
                }).then(response => {
                    if (response) {
                        this.isPassChangedPopupVisible = true
                        console.log(response)
                    }
                }).catch(error => {
                    if (error.data.current_password) {
                        this.error_old_pass = [...error.data.current_password]
                    }

                    if (error.data.new_password) {
                        this.error_new_pass = [...error.data.new_password]
                    }

                    console.log(error)
                })
            }
            this.error_old_pass = []
            this.error_new_pass = []
            this.error_new_pass_repeat = []

            if (!this.old_pass) {
                this.error_old_pass.push('Пустое поле');
            }
            if (!this.new_pass) {
                this.error_new_pass.push('Пустое поле');
            }
            if (!this.new_pass_repeat) {
                this.error_new_pass_repeat.push('Пустое поле');
            } else{
                if (this.new_pass!=this.new_pass_repeat){
                    this.error_new_pass_repeat.push('Пароли не совпадают')
                }
            }
            this.errors++;
            e.preventDefault();
        },
    },
    mounted() {
    },
}