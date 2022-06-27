import api_wrapper
import data


api = api_wrapper.Wrapper()


def fetch():
    fetch_skins()


def fetch_skins():
    for skin in api.skins():
        data.Skin.save(skin)
