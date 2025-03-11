import json
from openai import OpenAI
import base64
import os
from config import API_KEY

client = OpenAI(api_key=API_KEY)