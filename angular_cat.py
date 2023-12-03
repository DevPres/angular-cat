from cat.mad_hatter.decorators import tool, hook, plugin
from .angular_magic_component import angular_magic_component_factory
# from pydantic import BaseModel
# from datetime import datetime, date

# class MySettings(BaseModel):
#     required_int: int
#     optional_int: int = 69
#     required_str: str
#     optional_str: str = "meow"
#     required_date: date
#     optional_date: date = 1679616000

# @plugin
# def settings_schema():
#     return MySettings.schema()


@tool
def get_angular_magic_component(input, cat):
    """Use this function when the request is to generate angular component.
    input is the user input."""

    amg = angular_magic_component_factory(input)

    return amg


@hook
def before_rabbithole_stores_documents(doc, cat):
    prompt = f'''Extract relevant text from this doc: {doc}'''
    return cat.llm(prompt)
