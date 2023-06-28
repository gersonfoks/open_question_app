import {Question} from "@/stores/questionsDecks";

export class QuestionService {
    question_deck_base_route: string;

    constructor(base_route: string) {
        this.question_deck_base_route = base_route;
    }

    async getQuestionDecks(): Promise<any> {
        return new Promise((resolve, reject) => {
            fetch(this.question_deck_base_route + '/get_question_decks', {
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

    async createQuestionDeck(name: string, description: string,  questions: Question[] = [] ): Promise<any> {

        return new Promise((resolve, reject) => {
            fetch(this.question_deck_base_route + '/create_deck', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                },
                body: JSON.stringify({
                    name: name,
                    description: description,
                    questions: questions.map((question)  => {
                        return {
                            question: question.question,
                            correct_answer: question.answer
                        }
                    })
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

    async deleteQuestionDeck(name: string): Promise<any> {
        return new Promise((resolve, reject) => {
            fetch(this.question_deck_base_route + '/delete_question_deck', {
                method: 'delete',
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                },
                body: JSON.stringify({
                    name: name
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