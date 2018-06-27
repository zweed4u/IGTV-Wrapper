#!/usr/bin/python3
import json
import requests


class IGTV:
    def __init__(self):
        self.session = requests.session()
        self.headers = {
            'X-IG-Connection-Type':           'WiFi',
            'X-IG-Capabilities':              '36r/dw==',
            'X-IG-App-ID':                    '400851683688926',
            'X-IG-ABR-Connection-Speed-KBPS': '0',
            'Accept-Language':                'en-US;q=1',
            'User-Agent':                     'igtv 50.0.0.52.188 (iPhone6,1; iOS 10_2; en_US; en-US; scale=2.00; gamut=normal; 640x1136) AppleWebKit/420+',
            'X-IG-Bandwidth-Speed-KBPS':      '0.000',
            'X-IG-Experimental-Bandwidth-Speed-KBPS': '',
            'X-IG-Connection-Speed':          '-1kbps',
            'Accept-Encoding':                'gzip, deflate',
            'Host':                           'i.instagram.com',
            'X-FB-HTTP-Engine':               'Liger',
            'Connection':                     'keep-alive'
        }

    def continue_as_logged_in_ig(self):
        # headers
        # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        data = {
            'signed_body':        '.{"adid":"","sessionid":"","device_id":"-"}',
            'ig_sig_key_version': '5'
        }
        return self.session.request('POST', 'https://i.instagram.com/api/v1/accounts/continue_as_instagram_login/', data=data, headers=self.headers)

    def switch_user_ig_login(self):
        headers = {
            'X-IG-Connection-Speed':          '-1kbps',
            'Content-Type':                   'application/x-www-form-urlencoded; charset=UTF-8',
            'X-IG-Connection-Type':           'WiFi',
            'X-IG-Capabilities':              '36r/dw==',
            'X-IG-Experimental-Bandwidth-Speed-KBPS':  'ci_peak_0_5=-0.001; interval_1_0=0.000; most_recent_weighted_average_transfer_rate=-0.001; ci_1_0_avg_ro=-0.001; ci_peak_5_0=-0.001; ci_0_1=-0.001; most_recent_average_transfer_rate=0.000; interval_0_5=0.000; ci_1_0=-0.001; ci_1_0_avg=-0.001; current_estimated_bandwith=0.000; ci_0_5_avg=-0.001; ci_0_1_avg=-0.001; interval_5_0=0.000; ci_0_5=-0.001; egma_video=-0.001; egma_media=-0.001; egma_images=-0.001; most_recent_bayesian_average_transfer_rate=0.000; last_estimated_bandwidth=0.000; ci_5_0_avg=-0.001; interval_0_1=0.000; ci_peak_1_0=-0.001; ci_5_0=-0.001; ci_0_5_avg_ro=-0.001',
            'X-IG-App-ID':                    '400851683688926',
            'X-IG-ABR-Connection-Speed-KBPS': '0',
            'Accept-Language':                'en-US;q=1',
            'User-Agent':                     'igtv 50.0.0.52.188 (iPhone6,1; iOS 10_2; en_US; en-US; scale=2.00; gamut=normal; 640x1136) AppleWebKit/420+',
            'X-IG-Bandwidth-Speed-KBPS':      '0.000',
            'Accept-Encoding':                'gzip, deflate',
            'Host':                           'i.instagram.com',
            'X-FB-HTTP-Engine':               'Liger',
            'Connection':                     'keep-alive'
        }
        data = {
            'signed_body':        '.{"reg_login":"0","password":"<REDACTED>","device_id":"-","username":"<REDACTED","adid":"","login_attempt_count":"0","phone_id":""}',
            'ig_sig_key_version': '5'
        }
        return self.session.request('POST', 'https://i.instagram.com/api/v1/accounts/login/', data=data, headers=headers)

    def get_tv_guide(self):
        return self.session.request('GET', 'https://i.instagram.com/api/v1/igtv/tv_guide/', headers=self.headers)

    def post_channel(self):
        data = {
            'signed_body':        '.{"max_id":"","id":"for_you","_uuid":"","_uid":"<REDACTED>","_csrftoken":""}',
            'ig_sig_key_version': '5'
        }
        return self.session.request('POST', 'https://i.instagram.com/api/v1/igtv/channel/', data=data, headers=self.headers)

    def mark_as_seen(self):
        data = {
            'signed_body':        '.{"_csrftoken":"","_uuid":"","_uid":"","seen_state":"{\"impressions\":{\"\":{\"view_progress_s\":0.}}}"}',
            'ig_sig_key_version': '5'
        }
        return self.session.request('POST', 'https://i.instagram.com/api/v1/igtv/write_seen_state/', data=data, headers=self.headers)

    def create_channel(self):
        data = {
            'signed_body':        '.{"nux_type":"igtv_onboarding","_uuid":"","_uid":"","_csrftoken":""}',
            'ig_sig_key_version': '5'
        }
        return self.session.request('POST', 'https://i.instagram.com/api/v1/nux/write_nux_type/', data=data, headers=self.headers)

    def search_channel(self, search_keyword):
        query_string = {
            'query':      search_keyword,
            'rank_token': ''  #id_uuid
        }
        return self.session.request('GET', 'https://i.instagram.com/api/v1/igtv/search/', params=query_string, headers=self.headers)

    def like(self, media_id):
        query_string = {'d': '0'}
        data = {
            'signed_body':        '.{"_csrftoken":"","_uuid":"-","_uid":"","media_id":""}',
            'ig_sig_key_version': '5'
        }
        return self.session.request('POST', f'https://i.instagram.com/api/v1/media/{media_id}/like/', params=query_string, data=data, headers=self.headers)

    def get_comments(self, media_id):
        query_string = {
            'can_support_threading': 'true'
        }
        return self.session.request('GET', f'https://i.instagram.com/api/v1/media/{media_id}/comments/', params=query_string, headers=self.headers)

    def mark_as_typing(self, media_id):
        data = {
            'signed_body':        '.{"_uuid":"","_uid":"","_csrftoken":""}',
            'ig_sig_key_version': '5'
        }
        return self.session.request('POST', f'https://i.instagram.com/api/v1/media/{media_id}/comment_typing/', data=data, headers=self.headers)

    def comment(self, media_id, comment):
        data = {
            'signed_body':        '.{"_csrftoken":"","_uuid":"","_uid":"","comment_text":"' + comment + '","idempotence_token":"","containermodule":"comments_v2_igtv"}',
            'ig_sig_key_version': '5'
        }
        return self.session.request('POST', f'https://i.instagram.com/api/v1/media/{media_id}/comment/', data=data, headers=self.headers)

    def like_comment(self, comment_id):
        data = {
            'signed_body':        '.{"_csrftoken":"","_uuid":"","comment_id":"' + comment_id + '","_uid":""}',
            'ig_sig_key_version': '5'
        }
        return self.session.request('POST', f'https://i.instagram.com/api/v1/media/{comment_id}/comment_like/', data=data, headers=self.headers)

    def unlike_comment(self, comment_id):
        data = {
            'signed_body':        '.{"_csrftoken":"","_uuid":"","comment_id":"' + comment_id + '","_uid":""}',
            'ig_sig_key_version': '5'
        }
        return self.session.request('POST', f'https://i.instagram.com/api/v1/media/{comment_id}/comment_unlike/', data=data, headers=self.headers)

    def delete_comment(self, media_id, comment_id):
        data = {
            'signed_body':        '.{"comment_ids_to_delete":"' + comment_id + '","_uuid":"","_uid":"","_csrftoken":""}',
            'ig_sig_key_version': '5'
        }
        return self.session.request('POST', f'https://i.instagram.com/api/v1/media/{media_id}/comment/bulk_delete/', data=data, headers=self.headers)

    def logout(self):
        data = {'device_id': ''}
        return self.session.request('POST', 'https://i.instagram.com/api/v1/accounts/logout/', data=data, headers=self.headers)


print(json.dumps(IGTV().continue_as_logged_in_ig().json(), indent=4))
