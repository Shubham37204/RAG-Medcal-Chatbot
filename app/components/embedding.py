from langchain_huggingface import HuggingFaceEmbeddings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException
logger = get_logger(__name__)

def get_embedding_model():
    try:
        logger.info("initiazing our hugging face")
        model=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        logger.info("Hugging embedding model loaded successfully")
        return model
    except Exception as e:
        error_msg=CustomException("error in loading emvedding model",e)
        logger.error(str(error_msg))
        raise error_msg