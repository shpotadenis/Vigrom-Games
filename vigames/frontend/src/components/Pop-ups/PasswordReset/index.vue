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
                <div class="field">
                <div>
                    <label for="new_pass_area" id="new_pass_title">Новый пароль</label>
                    <error-message :error="error_new_pass[0]"
                                   v-show="error_new_pass.length>0">
                    </error-message>
                </div>
                <input
                        name="new_pass"
                        :type="typeconf"
                        id="new_pass_area"
                        placeholder="Введите новый пароль"
                        v-model="new_pass"
                >
                </div>
                <div>
                <div>
                    <label for="repeat_new_pass_area" id="repeat_new_pass_title">Повторите новый пароль</label>
                    <error-message :error="error_new_pass_repeat[0]"
                                   v-show="error_new_pass_repeat.length>0">
                    </error-message>
                </div>
                <input
                        name="repeat_new_pass"
                        :type="typeconf_repeat"
                        id="repeat_new_pass_area"
                        placeholder="Повторите новый пароль"
                        v-model="new_pass_repeat"
                >
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