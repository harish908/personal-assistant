# personal-assistant

Personal assistant to answer all your questions. With LLMs you can build your question-answering system! Train an LLM on a vast corpus of knowledge, such as Wikipedia or domain-specific data, and develop a system that can provide accurate and informative answers to user queries.

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
