# personal-assistant

Personal assistant to answer all your questions. With LLMs you can build your question-answering system! Train an LLM on a vast corpus of knowledge, such as Wikipedia or domain-specific data, and develop a system that can provide accurate and informative answers to user queries. 

Train model with your personalized content.
POST http://127.0.0.1:5000/api/transformText
Body:
{
  "data" : "data for training model"
}

Get answer for you question.
http://127.0.0.1:5000/api/prompt?data=Enter_your_question
