"""
Given list of captions, find stats about their ratings
"""
import pandas as pd
import os, sys

# send what lambda and R are
# get test script ready

def print_summary_file_for_contest(captions_file, query_file, summary_file,
                                   algorithm='LilUCB'):
    # with open(captions_file, 'r') as f:
        # captions = [caption.strip('\n') for caption in f.readlines()]
    # captions = {caption: {'Unfunny':0, 'Somewhat funny':0, 'Funny':0} for caption in captions}

    value_rating = {1: 'Unfunny',
                    2: 'Somewhat funny',
                    3: 'Funny'}

    captions = {}
    with open(query_file, 'r') as f:
        # f = open(query_file, 'r')
        for i, response in enumerate(f.readlines()):
            response = response.strip('\n').split(',', maxsplit=6)
            caption, rating, alg_label = response[-1], response[-3], response[-2]
            if algorithm.lower() in alg_label.lower() or \
                    alg_label.lower() in algorithm.lower():
                rating = int(float(rating))
                if not caption in captions.keys():
                    captions[caption] = {'Unfunny':0, 'Somewhat funny':0,
                            'Funny':0}
                captions[caption][value_rating[rating]] += 1
    # f.close()
    print(len(captions.keys()))
    import pandas as pd

    #  global df
    #  df = pd.DataFrame(captions).T
    #  df = df.sort()
    #  print(df)

    with open(summary_file, 'w') as f:
        print('Unfunny,Somewhat funny,Funny,Caption', file=f)
        total_ratings = 0
        for caption in captions:
            # print(caption)
            ratings = [int(captions[caption][rating]) for rating in ['Unfunny', 'Somewhat funny', 'Funny']]
            row = [str(rating) for rating in ratings]
            total_ratings += sum(ratings)
            print("{},{},{},{}".format(*row, caption), file=f)
    print("{} answers".format(total_ratings))


captions_file = '../adaptive-only-contests/526/526_captions_output.txt'
query_file = '../adaptive-only-contests/526/participant-responses.csv'
summary_file = '526_summary_LilUCB.csv'
algorithm = 'LilUCB'

print_summary_file_for_contest(captions_file, query_file, summary_file)

# contests_dir = '../contests/'
# for exp in os.listdir(contests_dir):
    # if 'DS' in exp or '.md' in exp or 'adaptive' in exp:
        # continue
    # if int(exp) < 510:
        # continue
    # if 'participant-responses.csv' in os.listdir(contests_dir + exp):
        # exp_dir = contests_dir + exp + '/'
        # captions_file = exp_dir + exp + '_captions.txt'
        # query_file = exp_dir + 'participant-responses.csv'
        # summary_file = exp + '_summary_{}.csv'.format(algorithm)

        # print_summary_file_for_contest(captions_file, query_file, summary_file,
                                       # algorithm=algorithm)

# for exp in os.listdir(contests_dir + 'adaptive-only-contests/'):
    # if 'DS' in exp or '.md' in exp:
        # continue
    # if 'participant-responses.csv' in os.listdir(contests_dir + 'adaptive-only-contests/' + exp):
        # exp_dir = contests_dir + 'adaptive-only-contests/' + exp + '/'
        # captions_file = exp_dir + exp + '_captions_output.txt'
        # query_file = exp_dir + 'participant-responses.csv'
        # summary_file = exp + '_summary_{}.csv'.format(algorithm)

        # print_summary_file_for_contest(captions_file, query_file, summary_file,
                                       # algorithm=algorithm)