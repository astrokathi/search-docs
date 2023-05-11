
# Search Docs using Open AI

This projects lets you index the documents (.xslx, .xls, .csv) using luecene indexing provided by [llama_index](https://pypi.org/project/llama-index/) and predict the prompts/ queries using LLMPredictor provided by Open AI's model `text-davinici-003` 

# Technical Specifications

* DRF (Django Rest Framework)
* Python 3.9 + 
* Any IDE for Python development (PyCharm)

# OPENAI_API_KEY (Linux/ Mac Setup)
* Open the `.bash_profile` in any editor of your choice.
* Then edit it by adding the below line 
    `export OPENAI_API_KEY=<Key Value>` at the end of the file.
* If there is no API key available, then you can create it from [API Key](https://platform.openai.com/account/api-keys), check the Usage and expiry date for the Open API Keys, if the Key is not valid, they will be no response provided and it will lead to `RateLimitErrors`.
* Once the above line is added to the `.bash_profile` file, then load it using the command `source ~/.bash_profile` and restart the terminal session.

# OPENAI_API_KEY (Windows Setup)
* Create a new environment variable from the Advanced System Settings.
* The name of the variable should be `OPENAI_API_KEY`, create it as a system/ user environment variable based on the administrator access and privileges.

# Setup Process

* Internet Connection (for resolving dependencies & accessing Github APIs)
* Checkout the [code](https://github.com/astrokathi/search-docs.git) or download a zip file.
* `cd` to the directory `search-docs`
* `pip install -r requirement.txt` to download all the dependencies.
* Once the packages are successfully installed, cd to the root directory where you can find `manage.py`
* By default a superuser is created with `kathi/ihtak` as username/password.
* To create a new superuser, execute `python manage.py createsuperuser` and follow the prompts.
* To use this newly created superuser to get the access tokens, change the username and password to the chosen values in the script of `index.html`
* Delete all contents inside the `data` folder, if you want only specific data to be indexed and the data which is already available is the sample data.
* To start the Server run, `python manage.py runserver`, this starts the server on the Port `8000` which is a default port and the home page is [Home](http://localhost:8000/home)

# Execution of prompts

* Open the [Homepage](http://localhost:8000/home) and upload the document.
* After the document is successfully uploaded, it will then be indexed and the Question input will be enabled.
* Ask for any question to get the response and check for the [Examples section](#examples)
* Don't rely completely on the Response, it's mostly accurate but, it is prone to errors. Please be wary of taking decisions solely on the response without a proper check.

# Examples
* What is this about? (You would get the response as a summary of what the uploaded document is about.)
* What are the colums of this dataset? (You would get the columns of the dataset)
* What is the mean/ average value of a `<your_column>`? (You would get the average value of that specific column)
* You could use the techniques involved in Prompt engineering to modify the prompts provided to get a more better and accurate responses which you could rely on.

# References

* [Prompt engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)
* Source [Github](https://github.com/wombyz/custom-knowledge-chatbot) for code inspiration.
* [Youtube](https://youtube.com) is a good source for learning LangChains, Search for `LangChains` or `llama_index with Open AI`

# Applications
* `llama_index` can index many things by default Out of the box from the package, for example, it can take the youtube URL and then read the transcripts, we can then query/ prompt about the video. Many other applications can be thought of to build a chatbot powered by Open AI.
