"use client";
import {Button, Col, Container, Row} from "react-bootstrap";
import {useContext, useState} from "react";
import {qaApiContext} from "@/app/contexts/context";


export default function QuestionAnswer() {
    const [answerContent, setAnswerContent] = useState(' ');

    const qaApi = useContext(qaApiContext);
    function handleClick() {
        console.log(answerContent);

        //
        console.log(qaApi.gradeAnswer('question', answerContent));

        // Do an api request to the backend to save the answer
    }

    return (
        <Container>

            <Row className={"justify-content-center "}>
                <Col lg="auto">
                    <h3>Question</h3>
                    <p>What is the meaning of life?</p>
                    <p>
                        <textarea name="answerContent"
                                  rows={4}
                                  cols={40}
                                  onChange={e => setAnswerContent(e.target.value)}/>
                    </p>

                    <Button variant="primary" onClick={handleClick}>
                        Submit
                    </Button>

                </Col>

            </Row>


        </Container>


    )
}
