import api_wrapper
import data


def setup():
    fetch_skins()
    fetch_account_skins()
    data.skins.setup()


def fetch_skins():
    for skin in api.skins():
        data.skins.save(skin)


def fetch_account_skins():
    data.skins.save_unlocked(api.account_skins())


if __name__ == '__main__':
    with open('key.txt') as f:
        key = f.readline().rstrip()
        api = api_wrapper.Wrapper(key)

    setup()
