import MessageSent from "../../../components/Pop-ups/MessageSent/index.vue"
import user from '../../../api/modules/user.js'

export default {
    name: "Support",

    components: {
      MessageSent
    },
    data() {
      return {
        isBtnClick: false,
          mail: null,
          mess: null,
          error_mail: []
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
            if (!this.mail) {
                this.error_mail.push('Пустое поле');
            }

            e.preventDefault()
        }
    }
}
