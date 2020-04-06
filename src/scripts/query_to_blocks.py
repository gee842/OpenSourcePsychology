import link_to_block_text as lb
import videos_by_cluster_name as vcluster

#Script to scrape by query, and save results to file.

if __name__ == '__main__':
    TEST_QUERY = 'anxiety'
    NUM_PER_QUERY = 5

    output_file = open(r"../script_output/search_output_" + TEST_QUERY + ".txt", "w+")
    final_out = ''
    video_jsons = vcluster.get_video_title_and_id_from_query(TEST_QUERY,NUM_PER_QUERY)
    for k,v in video_jsons.items():
        video_id = k
        video_title = v
        video_transcript = lb.id_to_punctuated_block(video_id)
        output_file.write(video_title + ':\n \n' + video_transcript + '\n \n')
    output_file.close()



