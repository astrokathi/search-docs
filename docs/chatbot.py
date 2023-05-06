import openai
import json
import os
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, LLMPredictor, PromptHelper, ServiceContext
from langchain import OpenAI


class Chatbot:
    #"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"
    def __init__(self, api_key, path):
        os.environ['OPENAI_API_KEY'] = api_key
        documents = SimpleDirectoryReader(path).load_data()
        # adding the LLM predictor with Open AI Engine

        # define LLM
        llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.1, model_name="text-davinci-003"))

        # define prompt helper
        # set maximum input size
        max_input_size = 4096
        # set number of output tokens
        num_output = 256
        # set maximum chunk overlap
        max_chunk_overlap = 20
        prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)

        service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)

        index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)

        # custom_LLM_index = GPTSimpleVectorIndex(
        #     documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
        # )
        self.index = index
        openai.api_key = api_key
        self.chat_history = []

    # os.path.join(os.getcwd(), 'data')

    def generate_response(self, user_input):
        prompt = "\n".join([f"{message['role']}: {message['content']}" for message in self.chat_history[-5:]])
        prompt += f"\nUser: {user_input}"
        query_engine = self.index.as_query_engine()
        response = query_engine.query(user_input)
        print("The response from the bot is {}".format(response))

        message = {"role": "assistant","query": user_input, "content": response.response}
        self.chat_history.append({"role": "user", "content": user_input})
        self.chat_history.append(message)
        return message

    def load_chat_history(self, filename):
        try:
            with open(filename, 'r') as f:
                self.chat_history = json.load(f)
        except FileNotFoundError:
            pass

    def save_chat_history(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.chat_history, f)
