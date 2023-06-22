<script lang="ts">
import {Question} from "@/stores/questionsDecks";

export default {
    inject: ['gradingService'],
    props: {
        question: {
            type: Question,
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

                <p>
                    <input type="text" class="form-control" placeholder="Answer" @change="updateAnswer">
                </p>
                <button class="btn btn-primary" @click="checkAnswer">
                    Check answer
                </button>
            </div>
            <div class="col" v-if="showAnswer">

                <h6>
                    Answer:
                </h6>

                <p>
                    {{ question.answer }}
                </p>

                <div>
                    <button class="btn btn-success m-1">
                        Correct
                    </button>

                    <button class="btn btn-danger">
                        Incorrect
                    </button>
                </div>

            </div>
            <div class="col" v-else>

            </div>


        </div>
    </div>


</template>
