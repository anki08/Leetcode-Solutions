import numpy as np
def maxEnvelopes(envelopes) -> int:
    envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
    print(envelopes)
    dp = np.ones(len(envelopes), dtype=int)
    val = [x[1] for x in envelopes]
    for i in range(len(val)):
        for j in range(i):
            if(val[i]> val[j] and val[i]> val[j] and dp[i] < dp[j]+1):
                dp[i] = dp[j]+1

    # print(dp)
    return max(dp)

if __name__ == '__main__':
    print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
    print(maxEnvelopes([[30,50],[12,2],[3,4],[12,15]]))