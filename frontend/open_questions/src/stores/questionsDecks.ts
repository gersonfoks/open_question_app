import {defineStore} from 'pinia'
import {QuestionService} from "@/service/QuestionDeckService";


export class Question {
    id: string;
    question: string;
    answer: string;

    constructor(question: string, answer: string) {
        this.question = question;
        this.answer = answer;
    }

}

export class QuestionDeck {
    id: string;
    name: string;
    description: string;
    questions: Question[];

    constructor(id: string, name: string, description: string, questions: Question[]) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.questions = questions;
    }

}


export const useQuestionDeckStore = defineStore('questionDeck', {
    state: () => ({
        questionDecks: [] as QuestionDeck[],
        questionDeckService: new QuestionService('http://localhost:8001')
    }),
    actions: {
        async getQuestionDecks() {
            return new Promise((resolve, reject) => {

                this.questionDeckService.getQuestionDecks().then((questionDecks) => {

                    this.questionDecks = questionDecks["decks"].map((questionDeck: any) => {
                        return new QuestionDeck(questionDeck["id"], questionDeck["name"], questionDeck["description"], questionDeck["question_ids"]
                        )
                    })
                    resolve(true)
                }).catch((error) => {
                    console.log(error)
                    reject(error)
                })
            })
        },
        async getDeckById(id: string) {
            return new Promise((resolve, reject) => {
                this.getQuestionDecks().then(() => {
                        resolve(this.questionDecks.find((questionDeck) => {

                            return questionDeck.id == id

                        }))
                    }
                )
            })
        },

        async getQuestionsById(ids: string[]) {
            return new Promise((resolve, reject) => {
                this.questionDeckService.getQuestionsByIds(ids).then((questions) => {
                    resolve(questions)
                })
            })
        },

        async createQuestionDeck(name: string, description: string, questions: Question[] = []) {
            return new Promise((resolve, reject) => {
                this.questionDeckService.createQuestionDeck(name, description, questions).then((id) => {
                    this.questionDecks.push(new QuestionDeck(id, name, description, questions))
                    resolve(true)
                }).catch((error) => {
                    console.log(error)
                    reject(error)
                })
            })
        },

        async deleteQuestionDeck(id: string) {
            return new Promise((resolve, reject) => {
                this.questionDeckService.deleteQuestionDeck(id).then(() => {
                    this.questionDecks = this.questionDecks.filter((questionDeck) => {
                        return questionDeck.id != id
                    })
                    resolve(true)
                }).catch((error) => {
                    console.log(error)
                    reject(error)
                })
            })
        },

        async addUserAnswer(questionId: string, answer: string, correct: boolean) {
            return new Promise((resolve, reject) => {
                this.questionDeckService.addUserAnswer(questionId, answer, correct).then(() => {
                    resolve(true)
                }).catch((error) => {
                    console.log(error)
                    reject(error)
                })
            })
        }


    }


})
