import CommentComponent from './CommentComponent/index.vue'
import user from '../../api/modules/user.js'

export default {
    name: "CommentsComponent",
    props: ['comments', 'newsData'],
    components: {
      CommentComponent
    },
    data() {
      return {
          commentFormShow: false,
          message: ''
      }
    },
    methods: {
        sendCommentClick() {
            user.createComment(this.newsData.id, {
                comment: this.message,
            }).then(response => {
                this.$emit('update-news')
                console.log(response)
            }).catch(error => {
                console.log(error)
            })
        },
    },
    computed: {

    }
}
