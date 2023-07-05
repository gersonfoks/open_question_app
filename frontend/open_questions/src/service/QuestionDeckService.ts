import {Question} from "@/stores/questionsDecks";

export class QuestionService {
    question_deck_base_route: string;

    constructor(base_route: string) {
        this.question_deck_base_route = base_route;
    }

    async getQuestionDecks(): Promise<any> {
        return new Promise((resolve, reject) => {
            fetch(this.question_deck_base_route + '/deck/get', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                }
            })
                .then(response => {

                    resolve(response.json());

                })
                .catch(error => {
                    console.log(error);
                    reject(error);
                })
        })
    }

    async createQuestionDeck(name: string, description: string, questions: Question[] = []): Promise<any> {

        return new Promise((resolve, reject) => {


            // First create all the questions
            fetch(this.question_deck_base_route + '/question/create_questions', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                },
                body: JSON.stringify({
                    questions: questions.map((question) => {
                        return {
                            question: question.question,
                            answer: question.answer
                        }
                    })
                })
            }).then((response) => {
                console.log(response)
                return response.json()

            }).then((response) => {

                fetch(this.question_deck_base_route + '/deck/create', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': '*',
                    },
                    body: JSON.stringify({
                        name: name,
                        description: description,
                        question_ids: response["ids"]
                    })
                }).then(response => {
                    resolve(response.json())

                })
                    .catch(error => {
                        console.log(error);
                        reject(error);
                    })
            })
        })


    }


    async deleteQuestionDeck(id: string): Promise<any> {
        console.log(id)
        return new Promise((resolve, reject) => {
            fetch(this.question_deck_base_route + '/deck/delete', {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                },
                body: JSON.stringify({
                    id: id
                })
            })
                .then(response => {
                    resolve(response.json());

                })
                .catch(error => {
                    console.log(error);
                    reject(error);
                })
        })

    }

    async getQuestionsByIds(ids: string[]): Promise<any> {
        return new Promise((resolve, reject) => {
            fetch(this.question_deck_base_route + '/question/get_questions', {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                },
                body: JSON.stringify({
                    question_ids: ids
                })
            })
                .then(response => {
                    const questions = response.json()
                    resolve(questions)
                })
                .catch(error => {
                    console.log(error);
                    reject(error);
                })
        })
    }

    async addUserAnswer(questionId: string, answer: string, correct: boolean): Promise<any> {
        return new Promise((resolve, reject) => {
            fetch(this.question_deck_base_route + '/question/add_answer', {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                },
                body: JSON.stringify({
                    question_id: questionId,
                    answer: answer,
                    correct: correct
                })
            })
                .then(response => {
                    resolve(response.json());

                })
                .catch(error => {
                    console.log(error);
                    reject(error);
                })
        })

    }

}