import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
books_df = pd.read_csv('BookDataSet/book.csv', sep=';', error_bad_lines=False, encoding="latin-1")#.head(10000)
books_df.drop(['Image-URL-M','Image-URL-L'],axis=1,inplace =True)
# print(books_df.columns,'\n')
users_df = pd.read_csv('BookDataSet/users.csv', sep=';', error_bad_lines=False, encoding="latin-1")#.head(10000)
# print(users_df.columns,'\n')
ratings_df = pd.read_csv('BookDataSet/book_ratings.csv', sep=';', error_bad_lines=False, encoding="latin-1")#.head(10000)
# print(ratings_df.columns,'\n')


# Task 1
# 1->python code for recommender system for similar books
# 2->loading data set to mongo
# 3->changing the recommender system such that it reads from mongo
# 4->API for connecting the recommender system code to node via .get and .post methods


rating_count = pd.DataFrame(ratings_df.groupby('ISBN')['Book-Rating'].count())
rating_count.sort_values('Book-Rating',ascending=False).head()

average_rating = pd.DataFrame(ratings_df.groupby('ISBN')['Book-Rating'].mean())#['Book-Rating'].mean()
average_rating['rating_count'] = pd.DataFrame(ratings_df.groupby('ISBN')['Book-Rating'].count())
average_rating.sort_values('rating_count',ascending=False).head() 



counts1 = ratings_df['User-ID'].value_counts()
ratings_df = ratings_df[ratings_df['User-ID'].isin(counts1[counts1 >=200].index)]
counts = ratings_df['Book-Rating'].value_counts()
ratings_df = ratings_df[ratings_df['Book-Rating'].isin(counts[counts>=50].index)] 


ratings_pivot = ratings_df.pivot(index='User-ID',columns='ISBN')['Book-Rating']

print(ratings_pivot.shape)

# userID = ratings_pivot.index
# ISBN = ratings_pivot.columns
# # print(ratings_pivot.shape)
# ratings_pivot.head()
# book_id = input('Enter book_id')
# given_book = ratings_pivot[book_id]
# similar_to_bones = ratings_pivot.corrwith(given_book)
# corr_bones = pd.DataFrame(similar_to_bones,columns=['pearsonR'])
# corr_bones.dropna(inplace=True)
# corr_summary = corr_bones.join(average_rating['rating_count'])
# corr_summary[corr_summary['rating_count']>=300].sort_values('pearsonR',ascending=False).head(10)

# # print(corr_summary.shape)


# rbooks = corr_summary[corr_summary['rating_count']>=300].sort_values('pearsonR',ascending=False).head(10).index
# rbooks = pd.DataFrame(rbooks)
# corr_books = pd.merge(rbooks, books_df, on='ISBN')
# print(corr_books['Book-Title'])