import { createRouter, createWebHistory } from 'vue-router'
import QuestionDecksView from '../views/QuestionDecksView.vue'
import PracticeQuestionsView from '../views/PracticeQuestionsView.vue'
import QuestionDeckEditorView from "@/views/questionDeckEditorView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: QuestionDecksView
    },
    {
      path: '/practice/:id',
      name: 'practice',
      component: PracticeQuestionsView,
      props: true
    },
    {
      path: '/edit/',
      name: 'edit',
      component: QuestionDeckEditorView,
      props: true
    },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue')
    // }
  ]
})

export default router
