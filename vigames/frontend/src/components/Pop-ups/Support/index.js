import MessageSent from "../../../components/Pop-ups/MessageSent/index.vue"
import user from '../../../api/modules/user.js'
import ErrorMessage from '../../ErrorMessageComponent/index.vue'

export default {
    name: "Support",

    components: {
      MessageSent,
        ErrorMessage
    },
    data() {
      return {
        isBtnClick: false,
          mail: null,
          mess: null,
          error_mail: [],
          error_mess: []
      }
    },
    methods:{
        checkForm(e){

            if (this.mail){
                this.error_mail = [];
                user.makeQuestion({
                    email: this.mail,
                    question: this.mess
                }).then(response => {
                    if (response) {
                        this.isBtnClick = true;
                    }

                }).catch(error => {
                    if (error.response.data.email) {
                        this.error_mail = [...error.response.data.email]
                    }
                })
                return true
            }
            this.error_mail = [];
            this.error_mess = [];
            if (!this.mail) {
                this.error_mail.push('*Обязательное поле');
            }
            if (!this.mess) {
                this.error_mess.push('*Обязательное поле');
            }

            e.preventDefault()
        }
    }
}
