// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
// import VueMaterial from 'vue-material';
import Vue from 'vue';
import VueCookie from 'vue-cookie'; // for cookie usage
import App from './app';


/* eslint-disable no-new */
Vue.use(VueCookie);

new Vue({
    el: '#app', /* To match the corresponding id in index.html*/
    template: '<App/>',
    components: { App },
});
