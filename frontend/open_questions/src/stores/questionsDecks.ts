import {defineStore} from 'pinia'


export interface Question {
    question: string;
    answer: string;

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

const demoQuestionDeck: QuestionDeck = {
    id: 1,
    name: "Demo Deck",
    questions: [
        {
            question: "What is the meaning of life?",
            answer: "42"
        },
        {
            question: "What is the capital of Germany?",
            answer: "Berlin"
        },
        {
            question: "Why would one use a state management library?",
            answer: "To avoid prop drilling"
        }]
}


const demoQuestionDeck2: QuestionDeck = {
    id: 2,
    name: "Demo Deck 2",
    questions: [
        {
            question: "What is the meaning of life?",
            answer: "42"
        },
        {
            question: "What is the capital of Germany?",
            answer: "Berlin"
        },
        {
            question: "Why would one use a state management library?",
            answer: "To avoid prop drilling"
        }]

}


export const useQuestionDeckStore = defineStore('questionDeck', {
    state: () => ({
        questionDecks: [] as QuestionDeck[],
    }),
    actions: {
        fetchQuestionDeck() {
            return new Promise((resolve, reject) => {
                setTimeout(() => {
                    this.questionDecks = [demoQuestionDeck, demoQuestionDeck2]
                    resolve(true)
                }, 1000)
            })
        }
    },

    getters: {
        getDeckById: (state) => {
            return (questionDeckId: number) => state.questionDecks.find((questionDeck) => questionDeck.id === questionDeckId)
        },
    },
})
