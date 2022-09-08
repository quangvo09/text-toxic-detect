from profanity_check import predict, predict_prob

print(predict(['nhucaidaubuoi']))
# [1]

print(predict(['xin chào']))
# [0]

print(predict(['dm']))
# [1]