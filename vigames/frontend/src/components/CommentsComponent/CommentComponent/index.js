import {getImageUrl} from "../../../utils";

export default {
    name: "CommentComponent",
    props: ['commentData'],
    computed: {
        getImage() {
            return getImageUrl(this.commentData.avatar)
        }
    }
}
