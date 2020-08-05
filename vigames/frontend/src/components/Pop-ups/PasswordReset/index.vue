<template>
    <div class="popup_wrapper">
        <div class="v_popup">
            <div class="v-popup_header">
                <p id="change_pass_title">Смена пароля</p>
                <img
                        id="exit_svg"
                        src="@/assets/img/exit_pass.svg"
                        alt="" @click="closePopup"
                >
                <img
                        id="line_svg"
                        src="@/assets/img/line_pass.svg"
                        alt=""
                >
                <div
                        @click="hide"
                >
                    <img
                            id="eye_pass"
                            src="@/assets/img/eye.png"
                            alt=""
                            v-show="!nonEye"
                    >
                    <img
                            id="eye_pass"
                            src="@/assets/img/eye-off.svg"
                            alt=""
                            v-show="nonEye"
                    >
                </div>
                <div
                        @click="hideconf"
                >
                    <img
                            id="eye_pass_second"
                            src="@/assets/img/eye.png"
                            alt=""
                            v-show="!nonEyeconf"
                    >
                    <img
                            id="eye_pass_second"
                            src="@/assets/img/eye-off.svg"
                            alt=""
                            v-show="nonEyeconf"
                    >
                </div>
                <div
                        @click="hideconf_repeat"
                >
                    <img
                            id="eye_pass_third"
                            src="@/assets/img/eye.png"
                            alt=""
                            v-show="!nonEyeconf_repeat"
                    >
                    <img
                            id="eye_pass_third"
                            src="@/assets/img/eye-off.svg"
                            alt=""
                            v-show="nonEyeconf_repeat"
                    >
                </div>
            </div>
            <div class="v-popup_content">
                <p id="old_pass_title">Старый пароль</p>
                <input
                        name="old_pass"
                        :type="type"
                        id="old_pass_area"
                        placeholder="Введите старый пароль"
                        v-model="old_pass"
                >
                <div
                        class="errors errors__old_pass"
                        v-if="error_old_pass.length"
                >{{error_old_pass[0]}}
                </div>
                <p id="new_pass_title">Новый пароль</p>
                <input
                        name="new_pass"
                        :type="typeconf"
                        id="new_pass_area"
                        placeholder="Введите новый пароль"
                        v-model="new_pass"
                >
                <div
                        class="errors errors__new_pass"
                        v-if="error_new_pass.length"
                >
                    {{error_new_pass[0]}}
                </div>
                <p id="repeat_new_pass_title">Повторите новый пароль</p>
                <input
                        name="repeat_new_pass"
                        :type="typeconf_repeat"
                        id="repeat_new_pass_area"
                        placeholder="Повторите новый пароль"
                        v-model="new_pass_repeat"
                >
                <div
                        class="errors errors__new_pass_repeat"
                        v-if="error_new_pass_repeat.length"
                >
                    {{error_new_pass_repeat[0]}}
                </div>
            </div>
            <div
                    class="v-popup_footer"
                    @click="SaveNewPass"
            >
                <button
                        id="save_change"
                        @click="checkForm"
                >Сменить пароль
                </button>
            </div>
        </div>
    </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>