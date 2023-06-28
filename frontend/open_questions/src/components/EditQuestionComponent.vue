<script lang="ts">


export default {

  props: {
    question: String,
    answer: String
  },
  emits: ['update:question', 'update:answer'],


  setup() {

  },

  data() {

  },
  methods: {}
}
</script>


<template>

  <div class="form-group mb3">
    <div class="row">
      <div class="col">
        <label for="Question" class="form-label">Question:</label>
        <input type="text" class="form-control" id="Question" placeholder="Question" :value="question"
               @input="$emit('update:question', $event.target.value)"
        />
      </div>
      <div class="col">
        <label for="Answer" class="form-label">Answer:</label>
        <input type="text" class="form-control" id="Answer" placeholder="Answer" :value="answer"
               @input="$emit('update:answer', $event.target.value)"
        />
      </div>
    </div>


  </div>

</template>
