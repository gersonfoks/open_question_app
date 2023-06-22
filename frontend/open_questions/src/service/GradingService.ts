export class GradingService {
    base_route: string;

    constructor(base_route: string) {
        this.base_route = base_route;
    }

    async gradeQuestion(question: number, correct_answer: string, your_answer: string): Promise<boolean> {
        return new Promise((resolve, reject) => {
            fetch(this.base_route + '/grade', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                },
                body: JSON.stringify({
                    question: question,
                    correct_answer: correct_answer,
                    your_answer: your_answer
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