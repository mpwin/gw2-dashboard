import api_wrapper
import data


api = api_wrapper.Wrapper()


def setup():
    fetch_skins()
    data.Skin.setup()


def fetch_skins():
    for skin in api.skins():
        data.Skin.save(skin)


if __name__ == '__main__':
    setup()
