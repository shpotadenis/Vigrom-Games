import FooterComponent from '../../components/FooterComponent/index.vue'
import v_popup from "../../../src/components/Pop-ups/ChangePass/index.vue"
import PasswordChanged from "../../../src/components/Pop-ups/PasswordChanged/index.vue"
import user from "../../api/modules/user";
import {getImageUrl} from "../../utils";

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
            pass: '',
            loading: false,
            avatarUrl: ''
        }
    },
    computed: {
      username() {
          return this.$store.getters['user/getUserName']
      },
      getAvatar() {
            if (typeof this.avatarUrl != 'string')
                return null
            else
                return getImageUrl(this.avatarUrl)
        }
    },
    beforeMount() {
        this.fetchData()
    },
    methods: {
        fetchData() {
            this.loading = true
            user.getAvatar().then(response => {
                this.avatarUrl = response.data
                this.loading = false
            }).catch(error => {
                console.log(error)
            })
        },
        setAvatar(event) {
            user.setAvatar({
                avatar: event.target.files[0]
            }).then(response => {
                if (response) {
                    this.fetchData()
                }
            }).catch(error => {
                console.log(error)
            })
        },
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