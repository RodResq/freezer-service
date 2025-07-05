import { initSnowFlake } from './snow_flake.js';
import { initResultadoPesquisa } from './modal/resultado_pesquisa.js'

document.addEventListener('DOMContentLoaded', function() {
    initSnowFlake();
    initResultadoPesquisa();
});