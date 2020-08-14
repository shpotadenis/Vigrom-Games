<template>
    <div v-if="!loading">
        <div class="editPage">
            <div class="title mainTitle">РЕДАКТИРОВАНИЕ</div>
            <div class="generalInfo container">
                <div class="partTitle">Основное</div>
                <div class="row ">
                    <div class="col-6">
                        <div class="blocks">
                            <div>
                                <label class="blockName" for="title">Название</label>
                                <error-message :error="error_name[0]"
                                               v-show="error_name.length>0">
                                </error-message>
                            </div>
                            <input class="textInputs nameInput"
                                   v-model="title"
                                   id="title"
                                   placeholder="Введите название"/>
                        </div>
                        <div class="blocks">
                            <div>
                                <label class="blockName" for="short_description">Краткое описание</label>
                                <error-message :error="error_shortDescription[0]"
                                               v-show="error_shortDescription.length>0">
                                </error-message>
                            </div>
                            <textarea class="textInputs thirdInpits"
                                      v-model="short_description"
                                      id="short_description"
                                      placeholder="Не более 440 символов"/>
                        </div>
                    </div>
                    <div class="col-6">
                        <div class="blocks">
                            <div>
                                <label class="blockName">Жанр</label>
                                <error-message :error="error_genre[0]"
                                               v-show="error_genre.length>0">
                                </error-message>
                            </div>
                            <div class="v-select">
                                <div
                                        class="genre_title"
                                        @click="areOptionsVisible = !areOptionsVisible"
                                >
                                    {{selected}}
                                    <img src="@/assets/img/genre-arrow.png" alt="" class="arrow">
                                </div>
                                <div
                                        class="options"
                                        v-if="areOptionsVisible"
                                >
                                    <p
                                            v-for="option in options"
                                            :key="option.value"
                                            @click="selectOption(option)"
                                    >
                                        {{option.name}}
                                    </p>
                                </div>
                            </div>
                        </div>

                        <div class="blocks">
                            <div>
                                <label class="blockName" for="price">Цена</label>
                                <error-message :error="error_price[0]"
                                               v-show="error_price.length>0">
                                </error-message>
                            </div>
                            <input class="textInputs priceInput"
                                   v-model="price"
                                   id="price"
                                   placeholder="Укажите цену в рублях"/>
                        </div>
                    </div>
                </div>
            </div>
            <div class="generalInfo container">
                <div class="partTitle">Загрузки</div>
                <div class="row ">
                    <div class="col-4">
                        <div class="blocks">
                            <div>
                                <label class="blockName">Картинка для карточки игры</label>
                                <error-message :error="error_img[0]"
                                               v-show="error_img.length>0">
                                </error-message>
                            </div>
                            <div class="form-group">
                                <label class="label">
                                    <span class="title">{{selectFile3}}</span>
                                    <input type="file" class="fileInput textInputs secondInputs"  @change="UpLoadFile3">
                                </label>
                            </div>
                        </div>
                        <div class="blocks">
                            <div>
                                <label class="blockName">Картинка для баннера</label>
                                <error-message :error="error_banner[0]"
                                               v-show="error_banner.length>0">
                                </error-message>
                            </div>
                            <div class="form-group">
                                <label class="label">
                                    <span class="title">{{selectFile2}}</span>
                                    <input type="file" class="fileInput textInputs secondInputs"  @change="UpLoadFile2">
                                </label>
                            </div>
                        </div>
                    </div>
                    <div class="col-4">
                        <div class="blocks">
                            <div>
                                <label class="blockName">Скриншоты</label>
                                <error-message :error="error_images[0]"
                                               v-show="error_images.length>0">
                                </error-message>
                            </div>
                            <div class="form-group">
                                <label class="label">
                                    <div class="AllName">
                                        <span class="title" v-for="(text,index) in array" :key="index">{{text.name}}</span>
                                    </div>
                                    <input type="file" class="fileInput textInputs secondInputs" v-on:change="UpLoadFile1" multiple>
                                </label>
                            </div>
                        </div>
                        <div class="blocks">
                            <div>
                                <label class="blockName" for="link">Ссылка на геймплей-видео</label>
                                <error-message :error="error_link[0]"
                                               v-show="error_link.length>0">
                                </error-message>
                            </div>
                            <input class="textInputs nameInput"
                                   v-model="youtube_link"
                                   id="link"
                                   placeholder="Укажите ссылку на Youtube"/>
                        </div>
                    </div>
                    <div class="col-4">
                        <div class="blocks">
                            <div>
                                <label class="blockName ">Архив с игрой для скачивания</label>
                                <error-message :error="error_file[0]"
                                               v-show="error_file.length>0">
                                </error-message>
                            </div>
                            <div class="form-group">
                                <label class="label">
                                    <div class="title">{{selectFile}}</div>
                                    <input type="file" class="fileInput textInputs secondInputs" @change="UpLoadFile">
                                </label>
                            </div>
                        </div>
                        <div class="col-11 tip">
                            Мы советуем добавить в архив инструкцию по установке игры.
                        </div>
                        <div class="col-11 tip">
                            *Обратите внимание, что размер архива не должен превышать 750 МБ.
                            В случае, если архив больше, свяжитесь с нами через службу поддержки и мы сами загрузим вашу игру на сайт.
                        </div>
                    </div>
                </div>
            </div>

            <div class="generalInfo container">
                <div class="partTitle">Полное описание игры</div>
                <div class="row">
                    <div class="col-6">
                        <div class="blocks">
                            <div>
                                <label class="blockName" for="block1">Блок 1</label>
                                <error-message :error="error_block1[0]"
                                               v-show="error_block1.length>0">
                                </error-message>
                            </div>
                            <textarea class="textInputs thirdInpits"
                                      id="block1"
                                      v-model="block1"
                                      placeholder="Не более 440 символов"/>
                        </div>
                        <div class="blocks">
                            <div>
                                <label class="blockName" for="block3">Блок 3</label>
                                <error-message :error="error_block3[0]"
                                               v-show="error_block3.length>0">
                                </error-message>
                            </div>
                            <textarea  class="textInputs thirdInpits"
                                       v-model="block3"
                                       id="block3"
                                       placeholder="Не более 440 символов"/>
                        </div>
                    </div>
                    <div class="col-6">
                        <div class="blocks">
                            <div>
                                <label class="blockName" for="block2">Блок 2</label>
                                <error-message :error="error_block2[0]"
                                               v-show="error_block2.length>0"
                                               class="error">
                                </error-message>
                            </div>
                            <textarea class="textInputs thirdInpits"
                                      id="block2"
                                      v-model="block2" placeholder="Не более 440 символов"/>
                        </div>
                        <div class="col-10 tip">
                            *Добавьте полное описание игры, разделив его на 3 блока,
                            каждый максимум по 440 символов
                        </div>
                        <button class="uploadBtn" @click="uploadButtonClick">Сохранить изменения</button>
                    </div>
                </div>
            </div>
        </div>
        <footer-component></footer-component>
    </div>
</template>

<script src="./index.js" type="application/javascript"></script>

<style scoped src="./index.css" rel="stylesheet"></style>
