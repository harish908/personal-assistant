import psycopg2
import pgvector
from pgvector.psycopg2 import register_vector
from psycopg2.extras import execute_values
from datetime import datetime

class PostgresDB:
    def DBConnect(self):
        try:
            self.DBConnection = psycopg2.connect(
                host="localhost",
                database="Gen_AI"
            )
            register_vector(self.DBConnection)
            print("Connected to the database.")
            
        except Exception as ex:
            print("Unable to connect to the database. Exception: ", ex)

    def DBDisconnect(self):
        self.DBConnection.close()
        print("Disconnected from the database.")

    def SaveEmbeddings(self, embeddings: list):
        try:
            cursor = self.DBConnection.cursor()
            current_time = datetime.now()
            dataList = [(embedding.content, embedding.embedding, embedding.tokens, current_time) for embedding in embeddings]
            execute_values(cursor, "INSERT INTO llm_embeddings (content, embedding, tokens, created_at) VALUES %s", dataList)
            self.DBConnection.commit()
            cursor.close()
            print("Embeddings saved successfully.")
            
        except Exception as ex:
            print("Issue while saving embeddings. Exception: ", ex)

    def GetSimilarEmbeddings(self, query_embedding: list) -> list:
        try:
            cursor = self.DBConnection.cursor()
            cursor.execute("SELECT content, created_at FROM llm_embeddings ORDER BY embedding <-> %s::vector LIMIT 100", (query_embedding,))
            records = cursor.fetchall()
            cursor.close()
            return records

        except Exception as ex:
            print("Issue while getting embeddings. Exception: ", ex)






# CREATE TABLE llm_embeddings (id SERIAL PRIMARY KEY, content text not null, embedding vector(768) not null, tokens integer not null, created_at TIMESTAMP WITH TIME ZONE NOT null);
# CREATE INDEX ON llm_embeddings USING ivfflat (embedding vector_l2_ops) WITH (lists = 100);    --- index for Euclidean distance (L2 distance)