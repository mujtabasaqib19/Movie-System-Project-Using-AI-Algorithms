# -*- coding: utf-8 -*-
"""Movie Rating Predictor, Genre Movie, Naive Bayes to Predict Movie duration (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V6yMvfG1_12wNk2YT43ElBBTKJ5Z3U4V

# PAI PROJECT K22-4005, K22-4115, K22-8721

# IMDB MOVIES TOP 1000
"""

#CELL 1
import pandas as pd

df=pd.read_csv("IMDB top 1000.csv")
df.tail()

#CELL2
import pandas as pd

df = pd.read_csv("IMDB top 1000.csv")
print(df.head())
print(df.isnull().sum())
df = df.dropna()
df = df.drop_duplicates()
text_columns = ['Title', 'Genre', 'Rate', 'Description', 'Cast', 'Info']
df[text_columns] = df[text_columns].apply(lambda x: x.str.strip() if x.dtype == "object" else x)

df.to_csv("IMDB top 1000.csv", index=False, inplace=True)
print(df.tail())

"""# Matplot Graphs"""

#CELL 3
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\mujta\\Desktop\\Cleaned_IMDB_Data.csv")

a = int(input("1 Pie Chart for certificate distribution \n2 Bar Chart for Movie Certificate\n3 Pie chart of Genres \n4 Scatter plot of Ratings\n5 Histogram of MetaScores\n6 Scatter plot between MetaScore and Ratings\n7.Subplot between Metascore and Rating\n8 lineplot of metascore and Rating\n9 Lineplopt of Ratings\n10 lineplot of MetaScore\n11 Multiple plot of ratings and metascore\nchoose an option: "))

if a == 1:
    # Plot pie chart for certificate distribution
    df1 = df[df['Certificate'].isin(['R', 'PG-13', 'G', 'PG', 'Not Rated', 'Approved', 'Passed'])]
    certificate_counts = df1['Certificate'].value_counts()

    colors = ['lightcoral', 'lightblue', 'g', 'hotpink', 'darkblue', 'r', 'y']
    explode = (0.1, 0, 0, 0, 0, 0, 0)

    plt.figure(figsize=(8, 8))
    plt.pie(certificate_counts, labels=certificate_counts.index, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode)
    plt.title('Distribution of Certificates')
    plt.show()

elif a == 2:
    # Plot bar chart for certificate distribution
    df1 = df[df['Certificate'].isin(['R', 'PG-13', 'G', 'PG', 'Not Rated', 'Approved', 'Passed'])]
    certificate_counts = df1['Certificate'].value_counts()

    colors = ['lightcoral', 'lightblue', 'g', 'hotpink', 'darkblue', 'r', 'y']

    plt.figure(figsize=(10, 6))
    certificate_counts.plot(kind='bar', color=colors)
    plt.title('Distribution of Certificates')
    plt.xlabel('Certificate')
    plt.ylabel('Count')
    plt.show()

elif a == 3:
    # Plot pie chart for top 10 genres distribution
    genres_df = df['Genre'].str.split(',', expand=True)
    genres_series = genres_df.stack().reset_index(drop=True)
    genre_counts = genres_series.value_counts()
    top_genres = genre_counts.head(10)

    plt.figure(figsize=(12, 12))
    plt.pie(top_genres, labels=top_genres.index, autopct='%1.1f%%', startangle=90, labeldistance=1.1, pctdistance=0.85)
    plt.xticks(rotation=45)
    plt.title('Distribution of Top 10 Genres')
    plt.tight_layout()
    plt.show()

elif a == 4:
    # Scatter plot of ratings
    plt.figure(figsize=(10, 10))
    plt.scatter(df.index, df['Rate'], marker="*", alpha=0.5, color='darkblue', linewidths=1.4)
    plt.grid(True)
    plt.title('Scatter Plot of Ratings')
    plt.xlabel('Index')
    plt.ylabel('Rating')
    plt.show()

elif a == 5:
    # Histogram of MetaScores
    plt.figure(figsize=(10, 6))
    plt.hist(df['Metascore'], bins=20, color='darkblue', edgecolor='white',label="Metascore")
    plt.title('Histogram of MetaScores')
    plt.xlabel('MetaScore')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

elif a == 6:
    # Scatter plot between MetaScore and Ratings
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Metascore'], df['Rate'], alpha=0.5, color='darkblue',label="Metascore and Rating")
    plt.title('Scatter Plot between MetaScore and Ratings')
    plt.xlabel('MetaScore')
    plt.ylabel('Rating')
    plt.legend()
    plt.grid(True)
    plt.show()

elif a == 7:
    fig,axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    # Plot Metascore on the first subplot
    axes[0].scatter(df['Metascore'], df['Rate'])
    axes[0].set_title('Scatter Plot: Metascore vs Ratings')
    axes[0].set_xlabel('Metascore')
    axes[0].set_ylabel('Ratings')

    # Plot Ratings on the second subplot
    axes[1].scatter(df['Rate'], df['Metascore'])
    axes[1].set_title('Scatter Plot: Ratings vs Metascore')
    axes[1].set_xlabel('Ratings')
    axes[1].set_ylabel('Metascore')

    plt.tight_layout()
    plt.show()

elif a == 8:
    #lineplot of metascore and Rating
    df = df.sort_values(by='Rate')
    plt.figure(figsize=(10, 6))
    plt.plot(df['Rate'], df['Metascore'], marker='o', linestyle='-', color='b')
    plt.xlabel('Ratings')
    plt.ylabel('Metascore')
    plt.title('Line Plot: Ratings vs Metascore')
    plt.grid(True)
    plt.show()

elif a == 9:
    df = df.sort_values(by='Rate')
    plt.figure(figsize=(10, 6))
    plt.plot(df['Rate'], marker='o', linestyle='-', color='b')

    plt.xlabel('Index')
    plt.ylabel('Ratings')
    plt.title('Line Plot: Ratings')
    plt.grid(True)
    plt.show()

elif a==10:
    #lineplot of metascore
    df = df.sort_values(by='Metascore')
    plt.figure(figsize=(10, 6))
    plt.plot(df['Metascore'], marker='o', linestyle='-', color='r')

    plt.xlabel('Index')
    plt.ylabel('Metascore')
    plt.title('Line Plot: Metascore')
    plt.grid(True)
    plt.show()

elif a==11:
    #multiple plot of ratings and
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Rate'], marker='o', linestyle='-', color='b', label='Rating')
    plt.plot(df.index, df['Metascore'], marker='o', linestyle='-', color='r', label='Metascore')
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.title('Line Plot: Ratings and Metascore')
    plt.legend()
    plt.grid(True)
    plt.show()


else:
    print("Invalid option. Please choose a number between 1 and 11.")

"""# Split Function/ strip/ creating seperate columns for votes, gross and stars and Director and Duration as integer"""

#CELL 4
df = pd.read_csv("IMDB top 1000.csv")
df[['Votes', 'Gross']] = df['Info'].str.split('|', expand=True)
df[['Director', 'Stars']] = df['Cast'].str.split('|', expand=True)
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Remove "Director:" ,"Votes:", "Gross:", and "Stars:"prefix and keep only the director's name, stars name and gross and votes of movie
df['Director'] = df['Director'].str.replace('Director: ', '')
df['Votes'] = df['Votes'].str.replace('Votes: ','')
df['Gross'] = df['Gross'].str.replace('Gross: ','')
df['Stars'] = df['Stars'].str.replace('Stars: ', '')

# Create additional columns with lowercase letters
df['Director_lower'] = df['Director'].str.lower()
df['Stars_lower'] = df['Stars'].str.lower()

#seperate coloumn for Duration as integer
df['duration_int'] = df['Duration'].str.extract('(\d+)').astype(float)
df['duration_int'] = df['Duration'].str.extract('(\d+)').astype(int)

df.to_csv("C:\\Users\\mujta\\Desktop\\Cleaned_IMDB_Data.csv", index=False)
df

#CELL 5
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from fuzzywuzzy import fuzz
import difflib
import re

df = pd.read_csv("C:\\Users\\mujta\\Desktop\\Cleaned_IMDB_Data.csv")
print("Select from Following Algorithms(1-4)\n")

while True:
    try:
        choice = int(input("1.Random Forest for Movie Prediction\n2.Naive Bayes for Movie Duration\n3.Search Movie according to Title or Rate\n4.Search Movie according to Genre\n5.Exit\n"))

        if choice == 1:
            df[['Votes', 'Gross']] = df['Info'].str.extract(r'Votes: ([\d,]+) \| Gross: (\$\d+\.\d+[MB]?)')
            df[['Director', 'Stars']] = df['Cast'].str.split('|', expand=True)
            df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
            df.to_csv("IMDB top 1000.csv", index=False)
            df['Title'] = df['Title'].str.lower()
            df['Director'] = df['Director'].str.lower()
            df['Duration'] = df['Duration'].str.extract('(\d+)').astype(float)
            df['Votes'] = df['Votes'].str.replace(',', '').astype(float)
            df['Gross'] = df['Gross'].replace('[\$,M]', '', regex=True).astype(float)
            user_movie_name = input("Enter the movie name: ").lower()
            user_director_name = input("Enter the director name: ").lower()
            similar_directors = [director for director in df['Director'].unique() if fuzz.partial_ratio(user_director_name, director) >= 80]
            director_movies = df[df['Director'].isin(similar_directors)]
            X = director_movies[['Duration', 'Votes']]
            y = director_movies['Rate']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
            rf_model.fit(X_train, y_train)
            user_duration_input = input("Enter the movie duration (in the format '152 min'): ")
            user_duration = float(re.search(r'\d+', user_duration_input).group()) if re.search(r'\d+', user_duration_input) else None
            user_votes = float(input("Enter the number of votes: "))
            user_input_features = [[user_duration, user_votes]]
            predicted_rating = rf_model.predict(user_input_features)
            print(f"The predicted rating for the given movie is: {predicted_rating[0]}")

        elif choice == 2:
            df['duration_int'] = df['Duration'].str.extract('(\d+)').astype(int)
            label_encoder = LabelEncoder()
            df['Director_encoded'] = label_encoder.fit_transform(df['Director_lower'])
            features = ['Director_encoded']
            target = 'duration_int'
            X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)
            model = GaussianNB()
            model.fit(X_train, y_train)
            director_name_input = input("Enter the director's name: ").lower()
            director_encoded_input = label_encoder.transform([director_name_input])[0]
            predicted_duration = model.predict([[director_encoded_input]])
            print(f'Predicted duration for a movie directed by {director_name_input}: {predicted_duration[0]} minutes')

        elif choice == 3:
            def correct_choice(user_input):
                closest_match = None
                max_similarity = 0.0
                for ch in choice:
                    similarity = difflib.SequenceMatcher(None, user_input.lower(), ch.lower()).ratio()
                    if similarity > max_similarity:
                        closest_match = ch
                        max_similarity = similarity
                if max_similarity >= 0.6:
                    return closest_match
                return user_input

            user_input = input("Enter your choice (1 for Rate, 2 for Title): ")
            corrected_choice = correct_choice(user_input)

            if "Rate" == corrected_choice:
                rat = int(input("Enter your rating from 1 to 10 about the movie you want to search"))
                df1 = df[df['Rate'] >= rat]
                print(df1)

            elif "Title" == corrected_choice:
                def correct_movie_title(user_input):
                    closest_match = difflib.get_close_matches(user_input, df["Title"], n=1, cutoff=0.6)
                    if closest_match:
                        return closest_match[0]
                    else:
                        return user_input

                user_input = input("Enter the movie title: ")
                corrected_title = correct_movie_title(user_input)
                matching_rows = df[df["Title"].apply(lambda x: corrected_title.lower() in x.lower())]
                print("Corrected Title:", corrected_title)
                print("Matching Rows:")
                print(matching_rows)

        elif choice == 4:
            genre_synonyms = {
                "Drama": ["Drama", "Melodrama", "Tragedy", "Theater", "Play"],
                "Crime": ["Crime", "Criminal", "Illegal", "Lawlessness", "Offense"],
                "Action": ["Action", "Adventure", "Excitement", "Thrill", "Stunt"],
                "Adventure": ["Adventure", "Exploration", "Journey", "Quest", "Expedition"],
                "Biography": ["Biography", "Life story", "Autobiography", "Memoir", "Life history"],
                "History": ["History", "Historical", "Past", "Antiquity", "Chronicle"],
                "Sci-Fi": ["Sci-Fi", "Science Fiction", "Futuristic", "Space Opera", "Speculative fiction"],
                "Romance": ["Romance", "Love story", "Affection", "Passion", "Heartfelt"],
                "Western": ["Western", "Wild West", "Cowboy", "Frontier", "Outlaw"],
                "Fantasy": ["Fantasy", "Imaginary", "Enchantment", "Magic", "Mythical"],
                "Thriller": ["Thriller", "Suspense", "Intense", "Exciting", "Tension"],
                "Animation": ["Animation", "Cartoon", "Animated", "Toon", "Anime"],
                "Family": ["Family", "Relatives", "Kin", "Household", "Lineage"],
                "War": ["War", "Conflict", "Battle", "Combat", "Hostility"],
                "Comedy": ["Comedy", "Humor", "Funny", "Amusing", "Lighthearted"],
                "Mystery": ["Mystery", "Enigma", "Puzzle", "Conundrum", "Secret"],
                "Music": ["Music", "Musical", "Melody", "Harmony", "Tune"],
                "Horror": ["Horror", "Terrifying", "Frightening", "Scary", "Spooky"],
                "Sport": ["Sport", "Athletics", "Physical activity", "Exercise", "Game"]
            }
            def correct_genre(user_input):
                closest_match = None
                max_similarity = 0.0
                for genres_list in df["Genre"].apply(lambda x: x.split(',')):
                    for genre in genres_list:
                        for key, values in genre_synonyms.items():
                            if user_input.lower() in [synonym.lower() for synonym in values]:
                                return key
                        similarity = difflib.SequenceMatcher(None, user_input.lower(), genre.lower()).ratio()
                        if similarity > max_similarity:
                            closest_match = genre
                            max_similarity = similarity

                if max_similarity >= 0.6:
                    return closest_match
                return user_input

            user_input = input("Enter the movie genre: ")
            corrected_genre = correct_genre(user_input)
            matching_rows = df[df["Genre"].apply(lambda x: corrected_genre.lower() in [genre.lower() for genre in x.split(',')])]
            print("Matching Rows:")
            print(matching_rows)

        elif choice == 5:
            print("Exit\n")
            break
        else:
            print("Invalid Choice, Enter Again from 1-5\n")

    except ValueError:
        print("Invalid input. Please enter a number.")