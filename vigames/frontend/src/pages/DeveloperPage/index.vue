<template>
    <div class="wrapper" v-if="!loading">
        <v_popup
                v-if="isInfoPopupVisible"
                @closePopup="closeInfoPopup"
                @SaveNewPass="SaveNewPass"
        >
        </v_popup>
        <div><p id="personal_account_title">Личный кабинет</p></div>
        <img src="@/assets/img/line.png" alt="line">
        <div id="personal_account_info">
            <div id="border_user_info">
                <div id="img_container">
                    <img :src="getAvatar" alt="ellipse" id="img_ellipse">
                    <div @click="$refs.file.click()" class="file_click">
                        <img src="@/assets/img/case.svg" alt="case" id="img_case">
                        <img src="@/assets/img/case_ring.svg" alt="case_ring" id="img_case_ring">
                        <input type="file" ref="file" style="display: none" @change="setAvatar">
                    </div>
                </div>
                <p id="border_user_info_title">Разработчик</p>
                <p id="border_user_info_title_username_now">{{username}}</p>
                <p id="border_user_info_title_username_change">Имя пользователя:</p>
                <p id="border_user_info_title_email_change">Пароль:</p>
                <form name=" application ">
                    <input name="name" type="text" id="change_username_placeholder" v-model="name" placeholder="Введите новое имя" required />
                    <input name="email" type="password" id="changer_email_placeholder" v-model="pass" placeholder="Введите пароль" required/>
                </form>
                <button class="change_button" @click="saveClick">Сохранить</button>
                <button
                        id="change_password"
                        @click="showPopupinfo"
                >
                    Изменить пароль
                </button>
            </div>
            <div id="control_panel">
                <p id="control_panel_title">Панель управления</p>
                <a class="control_panel_list" id="control_panel_title_first" @click="games = true">Мои игры</a>
                <my-games v-if="games" @close="games = false"></my-games>
                <router-link :to="{name: 'uploadPage'}">
                    <button id="control_panel_button">Загрузить игру</button>
                </router-link>
                <button class="change_button exit_btn" @click="quit">Выход</button>
            </div>
        </div>
        <footer-component></footer-component>
    </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>