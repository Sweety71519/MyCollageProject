from rest_framework.renderers import JSONRenderer

class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        wrapped_data = [data]  # wrap the data in a list
        return super().render(wrapped_data, accepted_media_type, renderer_context)
