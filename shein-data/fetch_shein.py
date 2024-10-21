import json

import requests

cookies = {
    'cookieId': 'DD63E8EB_DC96_6374_299F_7724F7C454AB',
    'AT': 'MDEwMDE.eyJiIjo3LCJnIjoxNzI5MzI0MjIyLCJyIjoiNERMZndkIiwidCI6MX0.849a21c32a911291',
    'RESOURCE_ADAPT_WEBP': '1',
    'armorUuid': '202410190250242e5579cd9a53600d5760c1803f55afb000bffb5e0f39a9cf00',
    'sessionID_shein': 's%3AHra5WYwKDdJVM9iixGlbxTYTjJZu8VSm.ACig0zFB9DBRFSYnbPyRM8saEMhi%2FKglRTwngWqJtok',
    '_cfuvid': 'nZA.79Zi1.95DU5FLWtbx_0wO_ghyu5FppjOJ8X2zp4-1729494684204-0.0.1.1-604800000',
    '_csrf': 'dHSKgRHqzABVi6oZDWqvXG9_',
    'jump_to_us': '1',
    'cf_clearance': 'EpjTbFl2Zve61SSehCDaxrHOPfcej7y_V6vzfv0EGK4-1729496072-1.2.1.1-9wwLyVnHhyvQNLVpSEDQN4i.Mzj5nBYH30HRYYog8jh_OqT27nEeAf7NVFyeFRbrLTAS5vMYITu0D.d2JxQbAy6e1EoY81fXtjrCQsybaJF_4mY6Xkr0_JAHsWS0p3qqiq6.T58wiZL00_c7XOq9wFiwYFsoerh0VgOtHdjYCLaYAYTH_c8lA4CSXlJglEDclzE5iAQ5_oe3EUgBD33y4ypN4IfryCtv1E8YJm2LjpBjJ_ibUxvBlcpaJI3gzL9hYzF3i.ZzJEdDUTwEBdLDqOQcaR46iGQ03xTzUaMcGM_B6f3x73f5lMocbxkVEP9Us9.HBWCsEMZMwfLFDb8sWL26MVN4jrxP1OLfWDVzR3AeSkpN2GwRQDHPrNGkSDPw',
    'smidV2': '202410210234321099cdb386581ff0cdb35f2622aa229a00653fa265c7d4f70',
    'forterToken': '6aaace24cd0542a38fba1f387977e1ac_1729496143373_73_UAS9b_17ck',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.5',
    'anti-in': '0_1.5.1_6da432_OOlfTlbLknNR5HD8lUMYFbNn0b3Muzce4_5LHtqplNRMLpWOgsl_v7APszFApRFvaV2PNHISZpxNIyuH4A-jvC9puwMLS-sxGuOuGoR8jj8yqbbw9DOgxzdngvUPRgZ4Zwx78_3_9LFe2_ecRc-qSozwFtNMHeaj19CoVb35KiOoRxtpDwEHaxFFQif1kr-3FaRVhrdCfnuWypqCo34U5Cs84hPTVflXH2Vabs6D_taJuWP-eofOCqOk7jNQSbOszw46diPHB7mIJdjxsGasSrtIA2DkX4VlKwqY5q879RRoJQTiyw-foqmVBe3FN-CezBP5oJX9884mwg-L0ukFAoM7CwfwYd4QTV5SKTqvkjoRMPzytihUW3e94gmr6yYMH1aC6tFDvg_Qv_swLQyR7DYzP9b__wEEFGSvF-yo0pG02dPqjgTab81g6xVymKNUN198qmZhVXEuMRDVEW0uSFfdJTeQ4FHS59zGmMdgvYelUfdKXZ04Jw1a5ijkr6QgQTzqwgk-lRjmHJ5sqvtqzg4aQyizY7M34x2DD2xLb6c64OhCxH2In0WJeDgpPc5ausjs8fx5W0jEdLjE4YY1rt_dbzNF4FHMrct97v-W99qTLr-O3UbGouO6iblLHCF_Y88VdvLyuci5bxOGUqHiDzEHXhDh38OrDDxHJL_KX18OPuI5yqOSW7urIoEwr-nN1',
    'armortoken': 'T0_3.0.1__OVWaW2LoRA-6IbpC2IFm9eeQTftK0ZrmnL59pdbFmZs6izlC1HGEv5L_cCg66j9lZPW5qs2x6Lv1-w66lvy2OcqZ5rUp7_MKObbfRyDiVXHEZE5G3btZZRDO40ciWhtvv9wpwPSv_vObjHP19XD6GlJ0-nPq97_zmk52HAmMzR7jsmvEW2XeFT2oC3lI1Q6_1729496137708',
    # 'cookie': 'cookieId=DD63E8EB_DC96_6374_299F_7724F7C454AB; AT=MDEwMDE.eyJiIjo3LCJnIjoxNzI5MzI0MjIyLCJyIjoiNERMZndkIiwidCI6MX0.849a21c32a911291; RESOURCE_ADAPT_WEBP=1; armorUuid=202410190250242e5579cd9a53600d5760c1803f55afb000bffb5e0f39a9cf00; sessionID_shein=s%3AHra5WYwKDdJVM9iixGlbxTYTjJZu8VSm.ACig0zFB9DBRFSYnbPyRM8saEMhi%2FKglRTwngWqJtok; _cfuvid=nZA.79Zi1.95DU5FLWtbx_0wO_ghyu5FppjOJ8X2zp4-1729494684204-0.0.1.1-604800000; _csrf=dHSKgRHqzABVi6oZDWqvXG9_; jump_to_us=1; cf_clearance=EpjTbFl2Zve61SSehCDaxrHOPfcej7y_V6vzfv0EGK4-1729496072-1.2.1.1-9wwLyVnHhyvQNLVpSEDQN4i.Mzj5nBYH30HRYYog8jh_OqT27nEeAf7NVFyeFRbrLTAS5vMYITu0D.d2JxQbAy6e1EoY81fXtjrCQsybaJF_4mY6Xkr0_JAHsWS0p3qqiq6.T58wiZL00_c7XOq9wFiwYFsoerh0VgOtHdjYCLaYAYTH_c8lA4CSXlJglEDclzE5iAQ5_oe3EUgBD33y4ypN4IfryCtv1E8YJm2LjpBjJ_ibUxvBlcpaJI3gzL9hYzF3i.ZzJEdDUTwEBdLDqOQcaR46iGQ03xTzUaMcGM_B6f3x73f5lMocbxkVEP9Us9.HBWCsEMZMwfLFDb8sWL26MVN4jrxP1OLfWDVzR3AeSkpN2GwRQDHPrNGkSDPw; smidV2=202410210234321099cdb386581ff0cdb35f2622aa229a00653fa265c7d4f70; forterToken=6aaace24cd0542a38fba1f387977e1ac_1729496143373_73_UAS9b_17ck',
    'priority': 'u=1, i',
    'referer': 'https://us.shein.com/RecommendSelection/Men-Clothing-sc-017172963.html?adp=&categoryJump=true&ici=us_tab06navbar06&src_identifier=fc%3DMen%20Clothing%60sc%3DMen%20Clothing%60tc%3D0%60oc%3D0%60ps%3Dtab06navbar06%60jc%3DitemPicking_017172963&src_module=topcat&src_tab_page_id=page_select_class1729496123249',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'smdeviceid': '',
    'uber-trace-id': 'ff0211e4cf9f8836:ff0211e4cf9f8836:0:0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-csrf-token': 'ARMpip8O-eMeQ5ViWNgBr93XPKH5dsnXhFRI',
    'x-gw-auth': 'a=xjqHR52UWJdjKJ0x6QrCsus66rNXR9@2.0.13&b=1729496148259&d=06942fbc37be6a98b8dee877d03ae8f6&e=RNc3xYWJmZTYzMGQyNjFkYjFiYWYyYzMxMDJkMWYxMzFlNDM1YjYxODljNWUxZTI2MzJjMTU2NDI0NGI5YzI2MmZlYQ%3D%3D',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    '_ver': '1.1.8',
    '_lang': 'en',
    'type': 'selection',
    'routeId': '017172963',
    'sub_type': 'RecommendSelection',
    'page': '1',
    'prePureGoods': '1',
    'categoryJump': 'true',
    'ici': 'us_tab06navbar06',
    'src_identifier': 'fc=Men Clothing`sc=Men Clothing`tc=0`oc=0`ps=tab06navbar06`jc=itemPicking_017172963',
    'src_module': 'topcat',
    'src_tab_page_id': 'page_select_class1729496123249',
    'requestType': 'firstLoad',
    'reqSheinClub': 'true',
    'isPaid': '0',
}

response = requests.get('https://us.shein.com/api/productList/info/get', params=params, cookies=cookies, headers=headers)

print(json.dumps(response.json(), indent=2))