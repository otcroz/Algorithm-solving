def solution(genres, plays):
    answer = []
    
    albums = [] # 앨범들을 저장할 공간
    count_genres = len(genres)
    for i in range(count_genres):
        albums.append((genres[i], plays[i], i))
    #print(albums)
    
    # 딕셔너리 생성: 베스트 앨범
    one_genres = list(set(genres))
    count_unique_genres = len(genres)
    blank_list = [[] for _ in range(count_unique_genres)]
    best_albums = dict(zip(one_genres, blank_list)) # (장르, 횟수, 번호)
    #print(best_albums)
    
    # 장르에 따라 딕셔너리에 추가 ()
    for i in range(count_genres):
        for key in best_albums.keys():
            if albums[i][0] == key:
                best_albums[key].append([albums[i][1], albums[i][2]])
                continue
    
    # 장르별 합 구한 뒤, (합, 장르) sort
    sum_plays = []
    for genre in one_genres:
        genre_sum = 0 # 장르별 합계 저장
        for item in best_albums[genre]:
            genre_sum += item[0]
        sum_plays.append((genre, genre_sum))
        
    sum_plays.sort(key=lambda x: -x[1]) # 장르별 재생 횟수 정렬
    print(sum_plays)
    for key in one_genres:
        best_albums[key].sort(key=lambda x: (-x[0], x[1])) # 횟수 내림, 번호 오름
    #print(best_albums)
    
    # 고유 번호 순서를 append
    for genre_play in sum_plays:
        genre = genre_play[0]
        best_albums[genre]
        #print(best_albums[genre])
        if len(best_albums[genre]) == 1: # 장르에 속한 곡이 1개
            answer.append(best_albums[genre][0][1])
            continue
        # 장르에 속한 곡이 2개 이상
        two_list = best_albums[genre][:2]
        for sing in two_list:
            answer.append(sing[1])
    
    return answer