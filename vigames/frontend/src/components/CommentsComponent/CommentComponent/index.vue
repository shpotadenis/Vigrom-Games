<template>
    <div>
        <div class="comments__card" :key="commentData.id">
            <div class="comments__userplate">
                <img src="@/assets/img/userpic.png" alt="avatar" class="userplate__pic" v-if="commentData.avatar == 'None'">
                <img :src="getImage" alt="avatar" class="userplate__pic" v-else>
            </div>
            <div class="comments__content">
                <div class="comments__header">
                    <h4 class="comments__username">{{commentData.user}}</h4>
                </div>
                <div class="comments__text">
                    <p>{{commentData.text_comment}}</p>
                </div>
            </div>
        </div>
        <comment-component v-for="(child, idx) in commentData.children_post"
                           :commentData="child"
                           :key="idx"
                           class="comments__card-child"
        ></comment-component>
    </div>
</template>

<script src="./index.js" />

<style scoped src="./index.css">
</style>