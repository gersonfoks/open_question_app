import {defineStore} from 'pinia'
import {QuestionService} from "@/service/QuestionDeckService";


export class Question {
    question: string;
    answer: string;

    constructor(question: string, answer: string) {
        this.question = question;
        this.answer = answer;
    }

}

export class QuestionDeck {
    name: string;
    description: string;
    questions: Question[];

    constructor(name: string, description: string, questions: Question[]) {

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
                    this.questionDecks = questionDecks["question_decks"].map((questionDeck: any) => {
                        return new QuestionDeck(questionDeck["name"], questionDeck["description"],
                            questionDeck["questions"].map((question: any) => {
                                return new Question(question["question"], question["answer"])
                            }))
                    })


                    resolve(true)
                }).catch((error) => {
                    console.log(error)
                    reject(error)
                })
            })
        },
        async getDeckByName(name: string) {
            return new Promise((resolve, reject) => {
                this.getQuestionDecks().then(() => {
                        resolve(this.questionDecks.find((questionDeck) => {

                            return questionDeck.name == name

                        }))
                    }
                )
            })
        },

        async createQuestionDeck(name: string, description: string ) {
            return new Promise((resolve, reject) => {
                this.questionDeckService.createQuestionDeck(name, description).then((questionDeck) => {
                    this.questionDecks.push(new QuestionDeck(name, description, []))
                    resolve(true)
                }).catch((error) => {
                    console.log(error)
                    reject(error)
                })
            })
        },

        async deleteQuestionDeck(name: string) {
            return new Promise((resolve, reject) => {
                this.questionDeckService.deleteQuestionDeck(name).then(() => {
                    this.questionDecks = this.questionDecks.filter((questionDeck) => {
                        return questionDeck.name != name
                    })
                    resolve(true)
                }).catch((error) => {
                    console.log(error)
                    reject(error)
                })
            })
        }
    }


})
