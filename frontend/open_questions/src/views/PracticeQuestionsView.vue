<script lang="ts">
import {Question, QuestionDeck, useQuestionDeckStore} from "@/stores/questionsDecks";
import * as _ from "lodash";
import QuestionComponent from "@/components/QuestionComponent.vue";

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
            type: Number,
            required: true
        }
    },
    data() {
        return {
            questionDeck: null as QuestionDeck | null,
            questions: null as Question[] | null
        }
    },
    mounted() {
        this.questionDeckStore.getDeckById(this.id).then((questionDeck: QuestionDeck) => {
            this.questionDeck = questionDeck

            this.questions = _.shuffle(questionDeck.questions)
        })

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

        <div v-else>
            <div v-for="question in questions"
                 class="row my-3 justify-content-center">
                <div class="col-8">
                    <QuestionComponent :question="question">
                    </QuestionComponent>
                </div>
            </div>
        </div>
    </div>


</template>
