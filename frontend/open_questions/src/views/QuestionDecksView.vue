<script setup lang="ts">

import 'bootstrap/dist/css/bootstrap.min.css'
import QuestionDeckCard from "@/components/QuestionDeckCard.vue";
import {QuestionDeck, useQuestionDeckStore} from "@/stores/questionsDecks";
import {storeToRefs} from "pinia";
import {reactive, ref} from "vue";

const questionDeckStore = useQuestionDeckStore()

const {questionDecks}= storeToRefs(questionDeckStore)


const state = reactive({
    questionDeckLoaded: false
})

questionDeckStore.fetchQuestionDeck().then(() => {
    state.questionDeckLoaded = true

})
console.log(questionDeckStore.fetchQuestionDeck())


</script>

<script lang="ts">


</script>

<template>

    <div class="py-5">
        <h3 class="text-center">
            Your question decks
        </h3>
    </div>


    <div class="container">

        <div v-if="!state.questionDeckLoaded">
            Loading...
        </div>

        <div v-else v-for="questionDeck in questionDecks" :key="questionDeck.id"
             class="row my-3 justify-content-center">
            <div class="col-4">
                <QuestionDeckCard :questionDeck="questionDeck as QuestionDeck">
                </QuestionDeckCard>
            </div>
        </div>


    </div>


</template>
