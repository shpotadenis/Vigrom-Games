import FooterComponent from '../../components/FooterComponent/index.vue'
import v_popup from "../../../src/components/Pop-ups/ChangePass/index.vue"
import PasswordChanged from "../../../src/components/Pop-ups/PasswordChanged/index.vue"

// TODO: Добавить валидацию
export default {
    name: 'PersonPage',
    components: {
        FooterComponent,
        v_popup,
        PasswordChanged,
    },
    data() {
        return {
            isInfoPopupVisible: false,
            isDownloadPopupVisible: false,
            name: '',
            pass: ''
        }
    },
    computed: {
      username() {
          return this.$store.getters['user/getUserName']
      }
    },
    methods: {
        showPopupinfo() {
            this.isInfoPopupVisible = true;
        },
        closeInfoPopup() {
            this.isInfoPopupVisible = false;
        },
        SaveNewPass() {
            this.isInfoPopupVisible = false;
            this.isDownloadPopupVisible = true;
        },
        close() {
            this.isDownloadPopupVisible = false;
        },

        saveClick(e) {
            if (this.name && this.pass) {
                this.$store.dispatch('user/changeName', {
                    username: this.name,
                    password: this.pass
                }).then(response => {
                    // TODO: Убрать отладочный вывод
                    console.log(response)
                }).catch(error => {
                    // TODO: Убрать отладочный вывод
                    // TODO: Добавить обработку ошибок
                    console.log(error)
                })
                return true
            }
            e.preventDefault()
        },
        becomeDev() {
            this.$store.dispatch('user/changeRole', {
                isDev: true
            }).then(response => {

                if (response) {
                    this.$router.push({
                        name: 'personPage'
                    })
                }

            }).catch(error => {
                // TODO: Убрать отладочный вывод
                console.log(error)
            })
        },
        quit() {
            this.$store.commit('user/userLogout')
            this.$router.push({
                name: 'homePage'
            })
        }
    }
}