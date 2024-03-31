# personal-assistant

Empower your inquiries with a personalized assistant capable of providing comprehensive answers. Utilized Large Language Models (LLMs) to construct a question-answering system. By training an LLM on extensive datasets like Wikipedia or domain-specific information, created a solution for delivering accurate and insightful responses to user questions.

#### Train model with your personalized content.
POST /api/transformText <br>
Body:
```
{
  "data" : "data for training model"
}
```

#### Get answer for you question.
GET /api/prompt?data=Enter_your_question
