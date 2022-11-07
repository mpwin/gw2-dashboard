import api_wrapper
import gw2_dashboard.data as data


def setup():
    print('Running setup...')

    fetch_skins()
    fetch_account_skins()

    data.collections.setup()
    data.skins.setup()

    print('Setup complete.')


def fetch_skins():
    print('Fetching skins...')

    for skin in api.skins():
        print(f"\tSkin {skin.get('id')} : {skin.get('name')}")
        data.skins.save(skin)

    print('Skins fetched.')


def fetch_account_skins():
    print('Fetching account skins...', end=' ')

    unlocked = api.account_skins()
    data.skins.save_unlocked(unlocked)

    print(f'{len(unlocked)} skins unlocked.')


if __name__ == '__main__':
    with open('key.txt') as f:
        key = f.readline().rstrip()
        api = api_wrapper.Wrapper(key)

    setup()
