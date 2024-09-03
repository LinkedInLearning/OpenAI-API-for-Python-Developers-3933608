import requests

def get_postcode(address):
    url = "https://postcode.teraren.com/postcodes.json"
    params = {'s': address}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # HTTPエラーがあれば例外を発生させる

        # JSONデータを解析
        postcodes = response.json()
        return [item['new'] for item in postcodes] if postcodes else "該当する郵便番号が見つかりません。"

    except requests.exceptions.HTTPError as errh:
        return "HTTP エラー: {}".format(errh)
    except requests.exceptions.ConnectionError as errc:
        return "接続エラー: {}".format(errc)
    except requests.exceptions.Timeout as errt:
        return "タイムアウトエラー: {}".format(errt)
    except requests.exceptions.RequestException as err:
        return "その他のエラー: {}".format(err)