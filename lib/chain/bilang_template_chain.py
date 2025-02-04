from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate, )
from langchain_core.prompts import MessagesPlaceholder

from lib.chain.prompt_registry import PromptRegistry


def get_bilang_template_chain(registry: PromptRegistry, chain_sink, kllm):
    bi_lang_template_system_prompt = registry.prompts['bi_lang_template_system_prompt']
    example_user_message_prompt = registry.prompts['example_user_message_prompt']
    example_assistant_message_prompt = registry.prompts['example_assistant_message_prompt']

    bilang_template_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", bi_lang_template_system_prompt),
            ("human", example_user_message_prompt),
            ("ai", example_assistant_message_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{question}"),
        ]
    )

    bilang_template_response = (
            bilang_template_prompt
            | kllm.get_deterministic_llm_runnable("bilang_template_answer", chain_sink)
            | StrOutputParser()
    ).with_config(run_name="BilangTemplateResponse")

    return bilang_template_response

