import PasswordReset from "../../../src/components/Pop-ups/PasswordReset/index.vue"
import PasswordChanged from "../../../src/components/Pop-ups/PasswordChanged/index.vue"
import ErrorMessage from '../../components/ErrorMessageComponent/index.vue'
import Support from '../../components/Pop-ups/Support/index.vue'

export default {
    name: "ForgotPass",
    components: {
        PasswordReset,
        PasswordChanged,
        ErrorMessage,
        Support
    },
    data() {
        return {
            support: false,
            isPassChangePopupVisible: false,
            first_btn: true,
            show_reset_pass: false,
            type: 'password',
            email: null,
            error_mail: [],
            errorMessage: '',
            allgood : false,
        }
    },
    methods: {
        hide() {
            if (this.allgood == true) {
                this.first_btn = false;
                this.show_reset_pass = true;
            }
        },
        closePopup() {
            this.show_reset_pass = false;
        },
        close() {
            this.isPassChangePopupVisible = false;
        },
        SaveNewPass() {
            this.show_reset_pass = false;
            this.isPassChangePopupVisible = true;
        },
        checkform(e) {
            this.error_mail = []

            if (this.email) {
                return this.allgood = true;
            }

            if (!this.email) {
                this.error_mail.push('*Обязательное поле');
            }
            e.preventDefault();
        }
    },
        computed: {}

}