import os
import datetime
import sys

import pandas as pd

def download(filename):
    # Download all reviewed changests from osmcha.
    url = 'http://osmcha.mapbox.com/?is_suspect=False&is_whitelisted=All&harmful=None&checked=True&all_reason=True&sort=-date&render_csv=True'
    changesets = pd.read_csv(url)

    # Filter changesets between October, 2015 and March, 2017.
    changesets['date'] = pd.to_datetime(changesets['date'])
    start_date = datetime.datetime(2015, 10, 1)
    end_date = datetime.datetime(2017, 3, 31)
    changesets = changesets[(changesets['date'] >= start_date) & (changesets['date'] <= end_date)]
    print('Changesets shape: {}'.format(changesets.drop_duplicates('ID').shape))

    # Write changesets to a file.
    changesets.to_csv(filename, index=False)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('\nUSAGE: python reviewed_changesets.py changesets.csv\n')
    else:
        download(sys.argv[1])
