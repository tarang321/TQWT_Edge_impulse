import numpy as np
from tqwt.tqwt import tqwt_radix2
import json
import sys

def extract_features(samples, sampling_rate):
    signal = np.array(samples)

    # TQWT parameters (tune these based on your use case)
    Q = 1.0
    r = 3.0
    J = 8

    subbands = tqwt_radix2(signal, Q, r, J)

    feature_vector = []
    feature_names = []

    for i, band in enumerate(subbands):
        feature_vector.extend([
            np.mean(band),
            np.std(band),
            np.max(band),
            np.min(band),
            np.median(band)
        ])
        feature_names.extend([
            f'subb{{i}}_mean',
            f'subb{{i}}_std',
            f'subb{{i}}_max',
            f'subb{{i}}_min',
            f'subb{{i}}_median'
        ])

    return {
        'features': feature_vector,
        'featureNames': feature_names
    }

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        data = json.load(f)

    values = data['payload']['values']
    sampling_rate = data['payload']['sampling_freq']

    result = extract_features(values, sampling_rate)
    print(json.dumps(result))