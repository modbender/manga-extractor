from urllib.parse import urlparse

from mext import enums, exceptions, providers


class Mext:

    def __init__(self, type_list: list, url: str):
        self.url = url
        self.type_list = self.validate_type_list(type_list)

        self.parsed_url = urlparse(url)

        data = self.get()

        for key, value in data.items():
            setattr(self, key, value)

    @property
    def all_providers(self):
        return providers.providers_json

    def validate_type_list(self, type_list):
        wrong_types = []
        for t in type_list:
            if t not in list(enums.Datacall.keys()):
                wrong_types.append(t)

        if wrong_types:
            raise ValueError(
                "Wrong fetch types provided: {}".format(wrong_types))

        return type_list

    def get(self):
        data = {}
        provider_instance = providers.get_provider_instance(
            netloc=self.parsed_url.netloc)
        provider_instance.process_url(self.url)
        for data_type in self.type_list:
            data[data_type] = getattr(
                provider_instance, enums.Datacall[data_type].value[0]
            )(self.url)

        if not data:
            raise exceptions.NotYetSupported(
                'The given URL is not supported right now.')

        return data
