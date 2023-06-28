<script lang="ts">

import {QuestionDeck, useQuestionDeckStore} from "@/stores/questionsDecks";
import {storeToRefs} from "pinia";
import {reactive} from "vue";
import QuestionDeckCard from "@/components/QuestionDeckCard.vue";
import AddQuestionDeckComponent from "@/components/AddQuestionDeckComponent.vue";

export default {
  computed: {
    QuestionDeck() {
      return QuestionDeck
    }
  },
  components: {QuestionDeckCard, AddQuestionDeckComponent},
  setup() {

    const questionDeckStore = useQuestionDeckStore()

    const {questionDecks} = storeToRefs(questionDeckStore)


    const state = reactive({
      questionDeckLoaded: false
    })

    questionDeckStore.getQuestionDecks().then(() => {
      state.questionDeckLoaded = true

    })

    return {
      state,
      questionDecks,
      questionDeckStore

    }
  },
  methods: {
    deleteDeck(name: string) {

      this.questionDeckStore.deleteQuestionDeck(name)
    }
  }
}


</script>

<template>

  <div class="py-5">
    <h3 class="text-center">
      Your question decks
    </h3>
  </div>

  <div class="container">

    <div class="row justify-content-center">
      <div class="col-3">
        <AddQuestionDeckComponent></AddQuestionDeckComponent>
      </div>

      <div class="col-4">
        <div v-if="!state.questionDeckLoaded">
          Loading...
        </div>


        <div v-else v-for="questionDeck in questionDecks" :key="questionDeck.name"
             class="row my-3">
          <div>
            <QuestionDeckCard :questionDeck="questionDeck as QuestionDeck" @deleteDeck="deleteDeck">
            </QuestionDeckCard>
          </div>
        </div>
      </div>


    </div>


  </div>


</template>
