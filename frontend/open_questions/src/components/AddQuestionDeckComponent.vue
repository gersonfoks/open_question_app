<script lang="ts">

import {useQuestionDeckStore} from "@/stores/questionsDecks";

export default {

    setup() {
        const questionDeckStore = useQuestionDeckStore()
        return {
            questionDeckStore
        }
    },

    data() {
        return {
            questionDeckName: "",
            description: ""

        }
    },
    methods: {
        updateName(event: any) {
            this.questionDeckName = event.target.value
        },

        updateDescription(event: any) {
            this.description = event.target.value
        },

        createDeck() {
            this.questionDeckStore.createQuestionDeck(this.questionDeckName, this.description)
            this.questionDeckName = ""
            this.description = ""
        }


    }
}
</script>


<template>

    <div class="container">
        <h5>
            Create a new question deck
        </h5>
        <p>
            <input type="text" class="form-control" placeholder="Question Deck Name" @change="updateName" :value="questionDeckName">
        </p>
        <p>
            <input type="text" class="form-control" placeholder="Question Deck description" @change="updateDescription"
            :value="description">
        </p>
        <button class="btn btn-primary" @click="createDeck">
            Create deck
        </button>

    </div>

</template>
