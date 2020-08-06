export default {
    name: "password_reset_popup",
    props: {
    },
    data() {
        return {
            type: 'password',
            typeconf: 'password',
            typeconf_repeat: 'password',
            nonEye: false,
            nonEyeconf: false,
            nonEyeconf_repeat: false,
            new_pass: null,
            new_pass_repeat: null,
            allgood: false,
            error_new_pass: [],
            error_new_pass_repeat: [],
            errors: 0
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
        checkForm(e){
            if (this.new_pass && this.new_pass_repeat && (this.new_pass_repeat==this.new_pass)) {
                this.allgood = true;
            }
            this.error_new_pass = []
            this.error_new_pass_repeat = []

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