from gemini_llm import GeminiLLM
from database import PostgresDB
import textwrap

class LLMService:
    def __init__(self, gemini: GeminiLLM, db: PostgresDB):
        self.Gemini_LLM = gemini
        self.DB = db

    def TransformText(self, data: str):
        formated_data = data.replace("'", "").replace('"', "").replace("\n", " ")
        embeddings = self.Gemini_LLM.GenerateEmbeddings(formated_data)
        self.DB.SaveEmbeddings(embeddings)

    def Prompt(self, query: str) -> str:
        query_embedding = self.Gemini_LLM.GenerateTextEmbedding(query)
        records = self.DB.GetSimilarEmbeddings(query_embedding)
        if records is None:
            return "No relevant answer found."

        relevant_passage = ""
        for record in records:
            relevant_passage += record[0] + ". "
        escaped = relevant_passage.replace("'", "").replace('"', "").replace("\n", " ")
        prompt = textwrap.dedent("""You are a helpful and informative bot that answers questions using text from the reference passage included below. \
        Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. \
        However, you are talking to a non-technical audience, so be sure to break down complicated concepts and \
        strike a friendly and converstional tone. \
        If the passage is irrelevant to the answer, you may ignore it.
        QUESTION: '{query}'
        PASSAGE: '{relevant_passage}'

            ANSWER:
        """).format(query=query, relevant_passage=escaped)
        return self.Gemini_LLM.Invoke(prompt)