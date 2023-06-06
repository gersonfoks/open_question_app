## Automatic grading and Question search

### 1. Introduction

This project is a demo on how one might do automatic grading of open answers as well as how to search for similar
questions in a database of questions.

### 2. Milestones

#### 2.1. Milestone 1: Automatic grading

As a milestone we want a simple backend + frontend that can do automatic grading of open answers.
We use some predefined questions and answers.

We create a simple one-page front-end as well as a simple backend that can do the following:

##### Backend:

- Create a simple api that can receive a question, example answer and a student answer and return a score.

##### Frontend:

- Create a simple page that shows several questions together and can make api requests for getting scores

#### 2.2. Milestone 2: Adding questions together with answers to a database

Create a persistent database in which we can add questions and answers

##### Backend:

Add an independent database to the backend that can store questions and answers. Together with student answers and
scores.

##### Frontend:

Add a page to the frontend that can add questions and answers to the database.

#### 2.3. Milestone 3: Searching for similar questions in the database

Store the questions together with the questions in a vector database and use this to search for similar questions.

##### Backend:

Add a vector database to the backend that can store questions and answers.
Each question and answer will be embedded and stored in this vector database.

##### Frontend:

Add a page to the frontend that can search for similar questions in the database.



