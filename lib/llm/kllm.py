from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq
from lib.utils.chain_output_sink import ChainOutputSink


class Kllm:
    def __init__(self):
        self.deterministic_llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.15)

    def get_deterministic_llm(self):
        return self.deterministic_llm

    def get_deterministic_llm_runnable(self, name, chain_sink: ChainOutputSink):
        return (RunnableLambda(lambda x: self.push_prompt(x, name, chain_sink))
                | self.deterministic_llm
                | RunnableLambda(lambda x: self.push_output(x, name, chain_sink)))

    def push_prompt(self, prompt: ChatPromptTemplate, prompt_name, chain_sink: ChainOutputSink):
        chain_sink.add_debug(
            name="prompt_" + prompt_name,
            content=[{"role": msg.type, "content": msg.content} for msg in prompt.messages]
        )
        return prompt

    def push_output(self, output: AIMessage, action_name, chain_sink: ChainOutputSink):
        chain_sink.add_debug(name=action_name, content=output.content)
        return output

