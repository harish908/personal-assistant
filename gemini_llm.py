from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

class TxtEmbedding:
    def __init__(self, content: str, embedding: list, tokens: int):
        self.content = content
        self.embedding = embedding
        self.tokens = tokens

class GeminiLLM:
    def __init__(self):
        self.Gemini_LLM = None
        self.LLM_Embeddings = None
        self.Text_Splitter = None

    def Connect(self):
        try:
            # Generate api key from https://aistudio.google.com/app/apikey
            self.Gemini_LLM = GoogleGenerativeAI(model="gemini-pro", temperature=0.9)  # By default it takes api key from GOOGLE_API_KEY environment variable
            self.LLM_Embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
            self.Text_Splitter = RecursiveCharacterTextSplitter(
                chunk_size=200,
                chunk_overlap=0, # Maximum characters that should overlap between two adjacent chunks
                separators = ['.'],
                keep_separator=False
            )
            print("Connected to gemini.")
        
        except Exception as ex:
            print("Issue while connecting to Gemini AI. Exception: ", ex)

    def GenerateEmbeddings(self, data: str) -> list:
        docs = self.Text_Splitter.split_text(data)
        vectors = self.LLM_Embeddings.embed_documents(docs)
        txtEmbedding = []
        for index, doc in enumerate(docs):
            txtTokens = self.GetTextTokens(doc)
            txtEmbedding.append(TxtEmbedding(doc, vectors[index], txtTokens))
        return txtEmbedding

    def GenerateTextEmbedding(self, text: str) -> list:
        return self.LLM_Embeddings.embed_query(text) 

    def GetTextTokens(self, text: str) -> int:
        return self.Gemini_LLM.get_num_tokens(text)

    def Invoke(self, query: str) -> str:
        return self.Gemini_LLM.invoke(query)