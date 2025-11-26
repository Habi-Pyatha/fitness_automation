from langchain import LLMChain, PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from app.schemas.parsers import ParsedWorkout
from langchain_google_genai import ChatGoogleGenerativeAI

