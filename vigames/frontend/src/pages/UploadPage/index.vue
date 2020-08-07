<template>
    <div>
        <div class="uploadPage">
            <div class="title">ЗАГРУЗКА ИГРЫ</div>
            <div class="generalInfo container">
                <div class="partTitle">Основное</div>
                <div class="row ">
                    <div class="col-6">
                        <div class="blocks">
                            <div class="blockName">Название</div>
                            <input class="textInputs nameInput" placeholder="Введите название"/>
                        </div>
                        <div class="blocks">
                            <div class="blockName">Краткое описание</div>
                            <textarea class="textInputs thirdInpits" placeholder="Не более 440 символов"/>
                        </div>
                    </div>
                    <div class="col-6">
                        <div class="blocks">
                            <div class="blockName">Жанр</div>
                            <select class="textInputs">
                                <option>Выберите жанр</option>
                                <option>Приключения</option>
                                <option>Головоломки</option>
                                <option>Экшн</option>
                                <option>РПГ</option>
                                <option>Стратегии</option>
                                <option>Фермы</option>
                                <option>ММО</option>
                                <option>Шутеры</option>
                                <option>Гонки</option>
                                <option>Симуляторы</option>
                            </select>
                        </div>
                        <div class="blocks">
                            <div class="blockName">Цена</div>
                            <input class="textInputs priceInput" placeholder="Укажите цену в рублях"/>
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
                                    <span class="title" v-for="text in a" :key="text.name">{{text}}</span>
                                    <input type="file" class="fileInput textInputs secondInputs" v-on:change="UpLoadFile1" multiple>
                                </label>
                            </div>
                        </div>
                        <div class="blocks">
                            <div class="blockName ">Ссылка на геймплей-видео</div>
                            <input class="textInputs secondInputs" placeholder="Укажите ссылку на Youtube"/>
                        </div>
                    </div>
                    <div class="col-4">
                        <div class="blocks">
                            <div class="blockName ">Архив с игрой для скачивания</div>
                            <div class="form-group">
                                <label class="label">
                                    <span class="title">{{selectFile}}</span>
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
                                <textarea class="textInputs thirdInpits" placeholder="Не более 440 символов"/>
                            </div>
                            <div class="blocks">
                                <div class="blockName">Блок 3</div>
                                <textarea class="textInputs thirdInpits" placeholder="Не более 440 символов"/>
                            </div>
                        </div>
                        <div class="col-6">
                            <div class="blocks">
                                <div class="blockName">Блок 2</div>
                                <textarea class="textInputs thirdInpits" placeholder="Не более 440 символов"/>
                            </div>
                            <div class="col-10 tip">
                                *Добавьте полное описание игры, разделив его на 3 блока,
                                каждый максимум по 440 символов
                            </div>
                            <input type="checkbox" class="agreement" id="agreement" name="agreement">
                            <label for="agreement">Я принимаю <a class="link"> пользовательсткое соглашение</a></label><br>
                            <button class="uploadBtn">Опубликовать игру</button>
                        </div>
                    </div>
            </div>
        </div>
        <footer-component></footer-component>
    </div>
</template>

<script src="./index.js" type="application/javascript"></script>

<style scoped src="./index.css" rel="stylesheet"></style>
