from . import settings

def get_content_models():
    return [model.rsplit(".", 1) for model in settings.CONTENT_MODELS]
        