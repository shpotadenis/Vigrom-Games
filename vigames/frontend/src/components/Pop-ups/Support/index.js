import MessageSent from "../../../components/Pop-ups/MessageSent/index.vue"

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
                this.isBtnClick = true;
                this.error_mail = [];
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
