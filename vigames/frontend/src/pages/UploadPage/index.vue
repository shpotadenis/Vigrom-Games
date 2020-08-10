<template>
    <div>
        <div class="uploadPage">
            <game-downloaded v-if="isBtnClick" @close="isBtnClick = false"></game-downloaded>
            <div class="title mainTitle">ЗАГРУЗКА ИГРЫ</div>
            <div class="generalInfo container">
                <div class="partTitle">Основное</div>
                <div class="row ">
                    <div class="col-6">
                        <div class="blocks">
                            <div class="blockName">Название</div>
                            <input class="textInputs nameInput" v-model="title" placeholder="Введите название"/>
                        </div>
                        <div class="blocks">
                            <div class="blockName">Краткое описание</div>
                            <input class="textInputs thirdInpits" v-model="short_description" placeholder="Не более 440 символов"/>
                        </div>
                    </div>
                    <div class="col-6">
                        <div class="blocks">
                            <div class="blockName">Жанр</div>
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
                            <div class="blockName">Платформа</div>
                            <div class="v-select">
                                <div
                                        class="genre_title"
                                        @click="areOptionsVisible_second = !areOptionsVisible_second"
                                >
                                    {{selected_two}}
                                    <img src="@/assets/img/genre-arrow.png" alt="" class="arrow">
                                </div>
                                <div
                                        class="options"
                                        v-if="areOptionsVisible_second"
                                >
                                    <p
                                            v-for="option in options_second"
                                            :key="option.value"
                                            @click="select_second_Option(option)"
                                    >
                                        {{option.name}}
                                    </p>
                                </div>
                            </div>
                        </div>
                        <div class="blocks">
                            <div class="blockName">Цена</div>
                            <input class="textInputs priceInput" v-model="price" placeholder="Укажите цену в рублях"/>
                        </div>
                    </div>
                </div>
            </div>
            <div class="generalInfo container">
                <div class="partTitle">Загрузки</div>
                <div class="row ">
                    <div class="col-4">
                        <div class="blocks">
                            <div class="blockName">Картинка для карточки игры</div>
                            <div class="form-group">
                                <label class="label">
                                    <span class="title">{{selectFile3}}</span>
                                    <input type="file" class="fileInput textInputs secondInputs"  @change="UpLoadFile3">
                                </label>
                            </div>
                        </div>
                        <div class="blocks">
                            <div class="blockName">Картинка для баннера</div>
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
                            <div class="blockName">Скриншоты</div>
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
                            <div class="blockName ">Ссылка на геймплей-видео</div>
                            <input class="textInputs secondInputs" v-model="youtube_link" placeholder="Укажите ссылку на Youtube"/>
                        </div>
                    </div>
                    <div class="col-4">
                        <div class="blocks">
                            <div class="blockName ">Архив с игрой для скачивания</div>
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
                                <div class="blockName">Блок 1</div>
                                <input class="textInputs thirdInpits" v-model="block1" placeholder="Не более 440 символов"/>
                            </div>
                            <div class="blocks">
                                <div class="blockName">Блок 3</div>
                                <input class="textInputs thirdInpits" v-model="block3" placeholder="Не более 440 символов"/>
                            </div>
                        </div>
                        <div class="col-6">
                            <div class="blocks">
                                <div class="blockName">Блок 2</div>
                                <input class="textInputs thirdInpits" v-model="block2" placeholder="Не более 440 символов"/>
                            </div>
                            <div class="col-10 tip">
                                *Добавьте полное описание игры, разделив его на 3 блока,
                                каждый максимум по 440 символов
                            </div>
                            <input type="checkbox" class="agreement" v-model="agreement" id="agreement" name="agreement">
                            <label for="agreement">Я принимаю <a class="link"> пользовательсткое соглашение</a></label><br>
                            <button class="uploadBtn" @click="uploadButtonClick">Опубликовать игру</button>
                        </div>
                    </div>
            </div>
        </div>
        <footer-component></footer-component>
    </div>
</template>

<script src="./index.js" type="application/javascript"></script>

<style scoped src="./index.css" rel="stylesheet"></style>
