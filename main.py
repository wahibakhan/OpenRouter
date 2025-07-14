from dotenv import load_dotenv
import os
from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,RunConfig
load_dotenv()
openrouter_api_key = os.getenv("openrouter_API_KEY")
# Check if the API key is present; if not, raise an error
if not openrouter_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=openrouter_api_key,
    base_url="https://openrouter.ai/api/v1",
)

model = OpenAIChatCompletionsModel(
    model="google/gemini-2.0-flash-exp:free", # example model replace  if needed
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
     
agent = Agent(
    name = "Writer Agent",
    instructions =  "you are a writer agent.Generate stories,poems,essay etc "
)

response = Runner.run_sync(
    agent,
    input="Write a short 6 paragraph essay on Allama Iqbal in simple and easy language",
    run_config=config
)

print(response)
   

