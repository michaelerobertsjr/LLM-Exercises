# import the required dependencies
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms import Ollama

# create the Ollama instance
llm = Ollama(
    model="mistral", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)

# use the Ollama instance to generate a response
print(llm("Tell me about the history of AI"))
