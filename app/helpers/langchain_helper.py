from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import Ollama

import os

phi3 = Ollama(model="phi3")


def generate(prompt, use_openai=False):
    """
    """
    # if use_openai:
    #     llm = OpenAI(temperature=0.1)
    # else:
    # prompt = PromptTemplate(template=text, input_variables=[""])
    # chain = LLMChain(llm=llm, prompt=prompt)
    # result = chain.run()
    for chunk in phi3.stream(prompt):
        print(f"chunk: {chunk}")
        yield chunk


if __name__ == "__main__":
    generate("python")