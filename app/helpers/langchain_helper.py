from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

import os



def generate_course_platform(course_name):
    llm = OpenAI(temperature=0.1)
    template = "Name 5 best platforms to learn {course_name}?"
    prompt = PromptTemplate(template=template, input_variables=["course_name"])
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(course_name=course_name)


if __name__ == "__main__":
    generate_course_platform("python")