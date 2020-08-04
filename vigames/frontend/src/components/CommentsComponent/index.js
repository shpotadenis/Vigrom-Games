const comments = [
    {
        id: 1,
        user_nickname: 'Имя Фамилия',
        text: 'Vivamus porta dignissim blandit. Mauris non libero sit amet mauris maximus pulvinar. Aliquam mattis vehicula metus, congue aliquam tellus euismod ultricies.'
    },
    {
        id: 2,
        user_nickname: 'Имя Фамилия',
        text: 'Vivamus porta dignissim blandit. Mauris non libero sit amet mauris maximus pulvinar. Aliquam mattis vehicula metus, congue aliquam tellus euismod ultricies.'
    },
    {
        id: 3,
        user_nickname: 'Имя Фамилия',
        text: 'Vivamus porta dignissim blandit. Mauris non libero sit amet mauris maximus pulvinar. Aliquam mattis vehicula metus, congue aliquam tellus euismod ultricies.'
    },
    {
        id: 4,
        user_nickname: 'Имя Фамилия',
        text: 'Vivamus porta dignissim blandit. Mauris non libero sit amet mauris maximus pulvinar. Aliquam mattis vehicula metus, congue aliquam tellus euismod ultricies.'
    }
]


export default {
    name: "CommentsComponent",
    computed: {
        getComments() {
            return comments;
        }
    }
}
