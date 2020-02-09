# 1) NLTK 라이브러리 설치 (pip install nltk)
import nltk
nltk.download('wordnet')

# 2) WordNet에서 동의어 얻기
from nltk.corpus import wordnet
print(wordnet.synsets('car'))
    # [Synset('car.n.01'), Synset('car.n.02'), Synset('car.n.03'), Synset('car.n.04'), Synset('cable_car.n.01')]
    # car(단어이름)/n(속성_명사,동사 등)/그룹의 인덱스

car = wordnet.synset('car.n.01')   # 동의어 그룹
print(car.definition())
print(car.lemma_names())    # 동의어 그룹에 속한 단어들의 이름을 얻을 수 있음.

# 3) WordNet과 단어 네트워크
# -> .hypernym_paths()
# WordNet을 구성하는 단어 네트워크는 위로 갈수록 추상적이고, 아래로 갈수록 구체적이 되도록 단어들을 배치.
# car.hypernym_paths()는 리스트를 반환.
print(car.hypernym_paths()[0])

# 4) WordNet을 사용한 의미 유사도
# -> .path.similarity()
# -> 단어 사이의 유사도를 0~1 범위의 실수로 반환(높을수록 비슷함)
# 노드 사이의 최소 거리를 활용
car = wordnet.synset('car.n.01')
novel = wordnet.synset('novel.n.01')
dog = wordnet.synset('dog.n.01')
motorcycle = wordnet.synset('motorcycle.n.01')

print(car.path_similarity(novel))
print(car.path_similarity(dog))
print(car.path_similarity(motorcycle))

# Leacock-Chodorow similarity
# 노드의 최소 거리 및 최대 깊이를 활용

# Wu-Porow similarity
# 깊이 및 최소 상위 노드 활용
