from TikTokApi import TikTokApi

#verifyFp = "verify_kq1n62rx_hGYo5C0T_fzt5_4LL8_9jP0_AKZHMykDx7UO"
#custom_verifyFP = verifyFp, use_test_endpoints=False
api = TikTokApi.get_instance()
tiktoks = api.trending(counts = 100)

for tiktok in tiktoks:
    print(tiktok['author']['uniqueId'])


def simple_dict(tiktok_dict):
  to_return = {}
  to_return['user_name'] = tiktok_dict['author']['uniqueId']
  to_return['user_id'] = tiktok_dict['author']['id']
  to_return['video_id'] = tiktok_dict['id']
  to_return['video_desc'] = tiktok_dict['desc']
  to_return['video_time'] = tiktok_dict['createTime']
  to_return['video_length'] = tiktok_dict['video']['duration']
  to_return['video_link'] = 'https://www.tiktok.com/@{}/video/{}?lang=en'.format(to_return['user_name'], to_return['video_id'])
  to_return['n_likes'] = tiktok_dict['stats']['diggCount']
  to_return['n_shares'] = tiktok_dict['stats']['shareCount']
  to_return['n_comments'] = tiktok_dict['stats']['commentCount']
  to_return['n_plays'] = tiktok_dict['stats']['playCount']
  return to_return

trending_videos = [simple_dict(v) for v in tiktoks]

import pandas as pd
trending_videos_df = pd.DataFrame(trending_videos)
trending_videos_df.to_csv('trending2.csv',index=False)
trending_videos_df['video_link']
trending_videos_df['video_id']
trending_videos_df['video_desc']