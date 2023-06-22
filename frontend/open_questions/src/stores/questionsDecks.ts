import {defineStore} from 'pinia'


export class Question {
    question: string;
    answer: string;

    constructor(question: string, answer: string) {
        this.question = question;
        this.answer = answer;
    }

}

export class QuestionDeck {
    id: number
    name: string;
    questions: Question[];

    constructor(id: number, name: string, questions: Question[]) {
        this.id = id;
        this.name = name;
        this.questions = questions;
    }

}

const demoQuestionDeck: QuestionDeck = new QuestionDeck(
    1,
    "Demo Deck 2",
    [
        new Question(
            "What is the meaning of life?",
            "42"
        ),
        new Question(
            "What is the capital of Germany?",
            "Berlin"
        ),
        new Question(
            "Why would one use a state management library?",
            "To avoid prop drilling"
        ),
        new Question(
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquid aspernatur corporis cumque laborum libero odit sed tempore unde. Molestias, repudiandae.",
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquid aspernatur corporis cumque laborum libero odit sed tempore unde. Molestias, repudiandae."
        ),

    ]
)


const demoQuestionDeck2: QuestionDeck = new QuestionDeck(
    2,
    "Demo Deck 2",
    [
        new Question(
            "What is the meaning of life?",
            "42"
        ),
        new Question(
            "What is the capital of Germany?",
            "Berlin"
        ),
        new Question(
            "Why would one use a state management library?",
            "To avoid prop drilling"
        ),
        new Question(
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquid aspernatur corporis cumque laborum libero odit sed tempore unde. Molestias, repudiandae.",
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquid aspernatur corporis cumque laborum libero odit sed tempore unde. Molestias, repudiandae."
        ),

    ]
)


export const useQuestionDeckStore = defineStore('questionDeck', {
    state: () => ({
        questionDecks: [] as QuestionDeck[],
    }),
    actions: {
        async fetchQuestionDeck() {
            return new Promise((resolve, reject) => {
                setTimeout(() => {
                    this.questionDecks = [demoQuestionDeck, demoQuestionDeck2]
                    resolve(true)
                }, 10)
            })
        },
        async getDeckById(questionDeckId: number) {
            return new Promise((resolve, reject) => {
                this.fetchQuestionDeck().then(() => {
                        resolve(this.questionDecks.find((questionDeck) => {

                            return questionDeck.id == questionDeckId

                        }))
                    }
                )
            })
        }


    },


})
