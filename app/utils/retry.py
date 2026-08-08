from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from litellm.exceptions import APIConnectionError, Timeout, RateLimitError, InternalServerError
    

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=8),
    retry=retry_if_exception_type((APIConnectionError, Timeout, RateLimitError, InternalServerError)),
    reraise=True,
)
def with_retry(func, *args, **kwargs):
    return func(*args, **kwargs)