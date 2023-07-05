<script lang="ts">
import {Question} from "@/stores/questionsDecks";

export default {
  inject: ['gradingService'],
  props: {
    question: {
      required: true
    }
  },

  data() {
    return {
      showAnswer: false,
      yourAnswer: "",
    }
  },
  methods: {
    updateAnswer(event: any) {
      this.yourAnswer = event.target.value
    },

    checkAnswer() {
      this.showAnswer = true
      this.gradingService.gradeQuestion(this.question.question, this.question.answer, this.yourAnswer).then(
          (response: any) => console.log(response)
      )
    }
  }

}


</script>


<template>

  <div class="container">

    <div class="row">
      <div class="col">

        <h6>
          Question:
        </h6>

        <p>
          {{ question.question }}
        </p>
        <form @submit.prevent="checkAnswer">
          <p>
            <input type="text" class="form-control" placeholder="Answer" :disabled="showAnswer" @change="updateAnswer">
          </p>
          <button class="btn btn-primary" @click="checkAnswer" type="submit" :disabled="showAnswer">
            Check answer
          </button>
        </form>


      </div>
      <div class="col" v-if="showAnswer">

        <h6>
          Answer:
        </h6>

        <p>
          {{ question.answer }}
        </p>

        <div>
          <h6 class="h6">Please grade your answer to go to the next question:</h6>
          <button class="btn btn-success m-1" @click="$emit('feedback', {'answer': yourAnswer, 'correct': true} )">
            Correct
          </button>

          <button class="btn btn-danger" @click="$emit('feedback', {'answer': yourAnswer, 'correct': false} )">
            Incorrect
          </button>
        </div>

      </div>
      <div class="col" v-else>

      </div>


    </div>
  </div>


</template>
