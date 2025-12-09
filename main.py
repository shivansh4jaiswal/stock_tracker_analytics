from connect_mysql import connect_to_db
from fetch_data import fetch_movie_data
from analysis import analyze_movies
from visualization import plot_results

def main():
    print("Connecting to database...")
    connection = connect_to_db()
    
    print("Fetching data...")
    data = fetch_movie_data(connection)
    
    print("Analyzing data...")
    analysis_results = analyze_movies(data)
    
    print("Generating visualizations...")
    plot_results(analysis_results)
    
    print("Done!")

if __name__ == "__main__":
    main()
