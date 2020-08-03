const reviews = [
    {
        id: 1,
        user_nickname: 'Name',
        title: 'Мой первый отзыв',
        rating: 3,
        text: 'Maecenas nec nunc lectus. Phasellus suscipit dui id rhoncus iaculis. Proin lobortis, enim nec condimentum vulputate, augue risus fermentum purus, ac pharetra orci justo nec tellus. Ut augue ex, laoreet in orci et, eleifend volutpat augue. Donec tempor dignissim diam blandit viverra. Praesent et neque blandit, ornare arcu imperdiet, tincidunt magna. Etiam sed fermentum lectus, vitae porta mauris. Proin pharetra enim eget enim facilisis, in facilisis enim tincidunt.'
    },
    {
        id: 2,
        user_nickname: 'Name',
        title: 'Мой второй отзыв',
        rating: 5,
        text: ' nec  lectus.   dui id  iaculis. Proin lobortis, enm nec  vulputate, augue risus fermentum purus, ac pharetra orci justo nec tellus. Ut augue ex, laoreet in orci et, eleifend volutpat augue. Donec tempor dignissim diam blandit viverra. Praesent et neque blandit, ornare arcu imperdiet, tincidunt magna. Etiam sed fermentum lectus, vitae porta mauris. Proin pharetra enim eget enim facilisis, in facilisis enim tincidunt.'
    },
    {
        id: 3,
        user_nickname: 'Name',
        title: 'Мой третий отзыв',
        rating: 2,
        text: 'mentum orci justo nec tellus. Ut augue ex, laoreet in orci et, eleifend volutpat augue. Donec tempor dignissim diam blandit viverra. Praesent et neque blandit, ornare arcu imperdiet, tincidunt magna. Etiam sed fermentum lectus, vitae porta mauris. Proin pharetra enim eget enim facilisis, in facilisis enim tincidunt.'
    },
    {
        id: 4,
        user_nickname: 'Name',
        title: 'Мой 4 отзыв',
        rating: 1,
        text: 'justo nec tellus. Ut augue ex, laoreet in orci et, eleifend volutpat augue. Donec tempor dignissim diam blandit viverra. Praesent et neque blandit, ornare arcu imperdiet, tincidunt magna. Etiam sed fermentum lectus, vitae porta mauris. Proin pharetra enim eget enim facilisis, in facilisis enim tincidunt.'
    }
]


export default {
    name: "ReviewsComponent",
    computed: {
        getReviews() {
            return reviews;
        }
    }
}