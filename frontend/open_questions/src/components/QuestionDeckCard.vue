<script lang="ts">
import {QuestionDeck} from "@/stores/questionsDecks";

export default {
    props: {
        questionDeck: {
            type: QuestionDeck,
            required: true
        }
    }
}


</script>


<template>

    <div class="card">
        <div class="card-header">
            <h5>
                {{ questionDeck.name }}
            </h5>
        </div>
        <div class="card-body">

            <p class="card-text">Questions about the meaning of life</p>
            <div class="text-center">
                <router-link :to="'/practice/' + questionDeck.id" class="btn btn-primary mx-1">Practice</router-link>
                <a href="#" class="btn btn-secondary mx-1">Edit</a>
            </div>

        </div>
    </div>

</template>
