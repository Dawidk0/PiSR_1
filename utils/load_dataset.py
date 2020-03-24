from pathlib import Path
import pandas

_ML_10M_DIR = Path('private') / 'ml-10M100K'


def load_dataset(dataset_dir=_ML_10M_DIR):
    movies_path = dataset_dir / 'movies.dat'
    ratings_path = dataset_dir / 'ratings.dat'
    tags_path = dataset_dir / 'tags.dat'

    sep = '::'
    movies_df = pandas.read_csv(movies_path, engine='python', sep=sep, header=0, names=['MovieID', 'Title', 'Genres'],
                                converters={'Genres': lambda x: tuple(x.split('|'))})
    ratings_df = pandas.read_csv(ratings_path, engine='python', sep=sep, header=0, names=['UserID', 'MovieID', 'Rating', 'Timestamp'])
    tags_df = pandas.read_csv(tags_path, engine='python', sep=sep, header=0, names=['UserID', 'MovieID', 'Tag', 'Timestamp'])
    return {'movies': movies_df, 'ratings': ratings_df, 'tags': tags_df}


if __name__ == '__main__':
    x = load_dataset()
    print(x['movies'])
    print(x['ratings'])
    print(x['tags'])
