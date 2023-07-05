<script lang="ts">
import {Question, QuestionDeck, useQuestionDeckStore} from "@/stores/questionsDecks";
import QuestionComponent from "@/components/QuestionComponent.vue";
import _ from "lodash";
export default {
  components: {QuestionComponent},
  setup: () => {
    const questionDeckStore = useQuestionDeckStore()
    return {
      questionDeckStore
    }
  },
  props: {
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      questionDeck: null as QuestionDeck | null,
      questions: null as Question[] | null,
      currentQuestionIndex: 0
    }
  },
  mounted() {
    this.questionDeckStore.getDeckById(this.id).then((questionDeck: QuestionDeck) => {
      this.questionDeck = questionDeck

      return this.questionDeck.questions
    }).then((question_ids: string[]) => {
      this.questionDeckStore.getQuestionsById(question_ids).then((questions: any) => {

        this.questions = _.shuffle(questions["questions"])
      })

    })
  },

  methods: {

    submitFeedback(e: Event) {
      this.questionDeckStore.addUserAnswer(this.questions[this.currentQuestionIndex].id, e['answer'], e['correct'])
      this.nextQuestionOrFinish()
    },

    nextQuestionOrFinish() {
      if (this.currentQuestionIndex == this.questions!.length - 1) {
        this.$router.push({name: "home"})
      } else {
        this.nextQuestion()
      }

    },
    nextQuestion() {
      this.currentQuestionIndex++
    },
    previousQuestion() {
      this.currentQuestionIndex--
    }
  }


}


</script>

<template>

  <div class="py-5">
    <h3 class="text-center">
      Practice Questions
    </h3>
  </div>

  <div class="container">
    <div v-if="!questionDeck">
      Loading...
    </div>

    <div v-else class="justify-content-center">
      <div v-for="(question, index) in questions">
        <div class="row justify-content-center">
          <div class="col-8">
            <QuestionComponent :question="question" v-show="index == currentQuestionIndex" @feedback="submitFeedback">
            </QuestionComponent>
          </div>

        </div>

      </div>

    </div>
  </div>


</template>
