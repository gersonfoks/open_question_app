"use client";
import {Accordion, Button, Col, Container, Row} from "react-bootstrap";
import QuestionAnswer from "@/app/components/question_answer";
import {qaApiContext} from "@/app/contexts/context";
import {QAApi} from "@/app/api/QAApi";


export default function Home() {


    const qaApi = new QAApi()
    return (


        <Container>

            <h1 className={"text-center"}>
                Open Questions
            </h1>

            <qaApiContext.Provider value={qaApi}>
                <QuestionAnswer></QuestionAnswer>
            </qaApiContext.Provider>


        </Container>

    )
}
