<script lang="ts">

import EditQuestionComponent from "@/components/EditQuestionComponent.vue";
import {useQuestionDeckStore} from "@/stores/questionsDecks";

export default {
  components: {EditQuestionComponent},
  setup() {
    const questionDeckStore = useQuestionDeckStore()
    return {
      questionDeckStore
    }

  },
  methods: {
    AddQuestion() {
      this.questions.push({
        question: "",
        answer: ""
      })
    },
    createDeck() {
      this.questionDeckStore.createQuestionDeck(this.name, this.description, this.questions)

    }
  },
  data() {

    return {
      name: "",
      description: "",
      questions: [
        {
          question: "",
          answer: ""
        },
        {
          question: "",
          answer: ""
        },
        {
          question: "",
          answer: ""
        },

      ]

    }

  }
  ,
}
</script>


<template>

  <div class="container mb-3">
    <h5>
      Create a new question deck
    </h5>
    <form>
      <div class="form-group mb-3">
        <label for="name" class="form-label">Question Deck Name: </label>
        <input type="text" class="form-control" id="name" placeholder="Question Deck Name" v-model="name"/>
      </div>

      <div class="form-group mb-3">
        <label for="description" class="form-label">Description:</label>
        <input type="text" class="form-control" id="description" placeholder="Question Deck Name"
               v-model="description"/>
      </div>

      <h6>
        Questions:
      </h6>
      <button @click="AddQuestion" type="button">
        Add question
      </button>
      <div class="overflow-y-scroll overflow-x-hidden question_area">
        <div v-for="q in questions">
          <EditQuestionComponent
              :question="q['question']"
              @update:question="newValue => q['question'] = newValue"
              :answer="q['answer']"
              @update:answer="newValue => q['answer'] = newValue"
          />
        </div>
      </div>


      <button type="button" class="btn btn-primary my-3" @click="createDeck">
        Create deck
      </button>


    </form>

  </div>


</template>

<style>

.question_area {
  height: 300px;

}

</style>