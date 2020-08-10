import CommentComponent from './CommentComponent/index.vue'

export default {
    name: "CommentsComponent",
    props: ['comments'],
    components: {
      CommentComponent
    },
    data() {
      return {
          commentFormShow: false,
          message: ''
      }
    },
    computed: {

    }
}
