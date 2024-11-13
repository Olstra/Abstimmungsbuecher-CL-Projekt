import os
from dotenv import load_dotenv

project_root = "Abstimmungsbuecher-CL-Projekt"


def get_config_info():
    """
    Gets the Config File path
    :return: The Path to the current config file
    """
    while True:
        if project_root in os.listdir():
            break
        os.chdir('..')
    load_dotenv()
    return {
        'openai-api-key': os.getenv('OPENAI_API_KEY')
    }


class Config:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True

        # initialize attributes
        data = get_config_info()
        self.gpt_api_key = str(data['openai-api-key'])

    def reload(self):
        """
        Reloads the config from the Environment
        :return: A instance of the Config
        """
        self.__init__()
        return self


# create unique instance of config
config_instance = Config()
