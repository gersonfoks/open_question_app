import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import provideServices from "@/service/services";


const app = createApp(App)



app.use(createPinia())
app.use(router)


provideServices(app)

app.mount('#app')
