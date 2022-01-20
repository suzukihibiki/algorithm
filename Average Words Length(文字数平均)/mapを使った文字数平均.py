
# mapメソッドを使う方法
def solution(sentence):
    for p in "!?',;.":
        sentence = sentence.replace(p, '')
    words = sentence.split()
    return round(sum(map(len, words))/len(words), 2)

sentence1 = "hi im hibi"
print(solution(sentence1))