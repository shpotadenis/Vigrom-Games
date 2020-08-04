import FooterComponent from '../../components/FooterComponent/index.vue'
import v_popup from "../../../src/components/Pop-ups/ChangePass/index.vue"
import PasswordChanged from "../../../src/components/Pop-ups/PasswordChanged/index.vue"


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
    }
}