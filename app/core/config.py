from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GROQ_API_KEY: str

    LLM_MODEL: str = "llama-3.3-70b-versatile"
    TEMPERATURE: float = 0.0
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    CHROMA_PERSIST_DIRECTORY: str = "./data/chroma_db"
    VECTOR_COLLECTION: str = "prod_rag"

    REDIS_URL: str = "redis://localhost:6379/0"

    CHUNK_SIZE: int = 800
    CHUNK_OVERLAP: int = 120

    RETRIEVAL_TOP_K: int = 20
    FINAL_TOP_K: int = 5

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()