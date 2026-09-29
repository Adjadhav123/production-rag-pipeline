from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GROQ_API_KEY: str

    LLM_MODEL: str = "qwen/qwen3.8-27b"
    EMBEDDING_MODEL:str = "nomic-embed-text"

    QDRANT_URL: str = "http://localhost:6333"
    QDRANT_COLLECTION: str = "prod_rag"

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