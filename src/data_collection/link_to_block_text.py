#This will be one of the numerous sources to feed the data lake

from youtube_transcript_api import YouTubeTranscriptApi


def link_to_id(link):
    for i in range(len(link)-1):
        if link[i] + link[i+1] == 'v=':
            return link[i+2:]

    raise Exception


def array_to_block(text_timestamp_array):
    # print(text_timestamp_array)
    returned_string = ''
    for i in text_timestamp_array:
        returned_string += i['text'] + ' '
    return returned_string


def array_to_punctuated_block(text_timestamp_array):
    print(text_timestamp_array)
    returned_string = ''
    punctuate = ' '
    for i in range(len(text_timestamp_array)-1):
        gap_length = (text_timestamp_array[i+1]['start'] + text_timestamp_array[i+1]['duration']) - (text_timestamp_array[i]['start'] + text_timestamp_array[i]['duration'])
        punctuate = ' ' if gap_length < 3 else '.\n'
        returned_string += text_timestamp_array[i]['text'].replace('.', '') + punctuate
    return returned_string


def link_to_block(link):
    video_id = link_to_id(link)
    if video_id != False:
        block_text = array_to_block(YouTubeTranscriptApi.get_transcript(video_id))
        return block_text
    else:
        raise Exception


def link_to_punctuated_block(link):
    video_id = link_to_id(link)
    if video_id != False:
        block_text = array_to_punctuated_block(YouTubeTranscriptApi.get_transcript(video_id))
        return block_text
    else:
        raise Exception

if __name__ == '__main__':
    TESTING_LINK = 'https://www.youtube.com/watch?v=9QiE-M1LrZk'
    # print(link_to_block(TESTING_LINK))
    print(link_to_punctuated_block(TESTING_LINK))