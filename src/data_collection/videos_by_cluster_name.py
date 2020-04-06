#Expected Input: name of disorder, Output: links with experiences of disorder Criteria: videos must have captions
from youtube_search import YoutubeSearch
import json

results = YoutubeSearch('search terms', max_results=10).to_json()


def generate_search_terms(query):
    templates = [f'My experiences with {query}', f'{query} symptoms', f'How it feels to have {query}', f'Living with {query}']
    return templates

def get_video_title_and_id_from_query(query,num_results = 5):
    vid_dict = {}

    terms = generate_search_terms(query)
    for i in terms:
        jsons_list = json.loads(YoutubeSearch(i,num_results).to_json())
        for item in jsons_list['videos']:
            vid_dict[item['id']] = item['title']
    return vid_dict

if __name__ == '__main__':
    print(get_video_title_and_id_from_query('anxiety'))