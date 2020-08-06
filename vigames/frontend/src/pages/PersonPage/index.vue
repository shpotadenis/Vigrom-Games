<template>
    <div class="wrapper">
        <v_popup
                v-if="isInfoPopupVisible"
                @closePopup="closeInfoPopup"
                @SaveNewPass="SaveNewPass"
        >
        </v_popup>
        <PasswordChanged
                v-if="isDownloadPopupVisible"
                @close="close"
        >
        </PasswordChanged>
        <div><p id="personal_account_title">Личный кабинет</p></div>
        <img src="@/assets/img/line.png" alt="line">
        <div id="personal_account_info">
        <div id="border_user_info">
            <div id="img_container">
            <img src="@/assets/img/Ellipse.svg" alt="ellipse" id="img_ellipse">
            <a href="http:yandex.ru">
            <img src="@/assets/img/case.svg" alt="case" id="img_case">
            <img src="@/assets/img/case_ring.svg" alt="case_ring" id="img_case_ring">
            </a>
            </div>
            <p id="border_user_info_title">Игрок</p>
            <p id="border_user_info_title_username_now">{{username}}</p>
            <p id="border_user_info_title_username_change">Имя пользователя:</p>
            <p id="border_user_info_title_email_change">Пароль:</p>
            <form name=" application ">
                <input name="name" type="text" id="change_username_placeholder" v-model="name" placeholder="Введите новое имя" required />
                <input name="email" type="password" id="changer_email_placeholder" v-model="pass" placeholder="Введите пароль" required/>
            </form>
            <button id="change_button" @click="saveClick">Сохранить</button>
            <button
                    id="change_password"
                    @click="showPopupinfo"
            >
                Изменить пароль
            </button>
        </div>
        <div id="control_panel">
        <p id="control_panel_title">Панель управления</p>
        <a href="" class="control_panel_list" id="control_panel_title_first">История покупок</a>
        <button id="control_panel_button" @click="becomeDev">Стать разработчиком</button>
        </div>
        </div>
        <footer-component></footer-component>
    </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>