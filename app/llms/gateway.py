from litellm import Router
from app.config.settings import get_settings

settings = get_settings()


model_list = [
    {
        "model_name": "primary-model",
        "litellm_params": {
            "model": "mistral/mistral-small-latest",
            "api_key": settings.MISTRAL_API_KEY,
        }
    },
    {
        "model_name": "fallback-model",
        "litellm_params": {
            "model": "gemini/gemini-2.5-flash",
            "api_key": settings.GEMINI_API_KEY,
        }
    }
]


router = Router(
    model_list=model_list,
    fallbacks=[
        {"primary-model": ["fallback-model"]}
    ],
    num_retries=2
)


def call_llm(prompt: str):
    response = router.completion(
        model="primary-model",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content




# def call_llm(prompt: str, response_format=None):

#     kwargs = {
#         "model": "primary-model",
#         "messages": [
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     }

#     if response_format:
#         kwargs["response_format"] = response_format

#     response = router.completion(**kwargs)

#     return response.choices[0].message.content