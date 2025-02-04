import streamlit as st

from lib.chain.prompt_registry import PromptRegistry
from lib.db.db_manager import DatabaseManager
from lib.utils.yaml_utils import load_yaml_file


@st.cache_resource
def config():
    return load_yaml_file("config/config.yml")['config']

def is_dev():
    return 'profile' not in config() or config()['profile'] == 'dev'

@st.cache_resource(show_spinner=False)
def db_manager():
    with st.spinner("Initializing..."):
        print("creating DB Manager")
        connection_string = "sqlite:///assistant.db"
        if not connection_string:
            raise ValueError("db.connection_string not provided!")

        return DatabaseManager(database_url=connection_string)


@st.cache_resource
def prompts_registry():
    return PromptRegistry()
