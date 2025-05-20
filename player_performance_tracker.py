import pandas as pd

def get_player_data():
    """
    Collects player data from user input.
    Returns a DataFrame with player stats.
    """
    records = []
    print("🏅 Enter player performance data (type 'done' to finish):")
    
    while True:
        name = input("Player name: ")
        if name.lower() == 'done':
            break
        try:
            matches = int(input("Matches played: "))
            goals = int(input("Goals scored: "))
            assists = int(input("Assists made: "))
            fouls = int(input("Fouls committed: "))
        except ValueError:
            print("Invalid input! Please enter numeric values for stats.")
            continue
        
        records.append({
            'Player': name.strip(),
            'Matches': matches,
            'Goals': goals,
            'Assists': assists,
            'Fouls': fouls,
            'Goals per Match': round(goals / matches, 2) if matches > 0 else 0,
            'Assists per Match': round(assists / matches, 2) if matches > 0 else 0,
            'Fouls per Match': round(fouls / matches, 2) if matches > 0 else 0,
        })
    
    return pd.DataFrame(records)

def display_summary(df):
    """
    Prints a summary of player performance.
    """
    print("\n📊 Player Performance Summary:\n")
    print(df.to_string(index=False))

    # Top performers
    top_goals = df.sort_values(by='Goals', ascending=False).head(1)
    top_assists = df.sort_values(by='Assists', ascending=False).head(1)

    print("\n🏆 Top Scorer:")
    print(top_goals[['Player', 'Goals']].to_string(index=False))

    print("\n🎯 Top Playmaker (Assists):")
    print(top_assists[['Player', 'Assists']].to_string(index=False))

def main():
    df = get_player_data()
    if df.empty:
        print("No data entered. Exiting.")
        return

    display_summary(df)

    save = input("\n💾 Do you want to save this summary to a CSV file? (yes/no): ")
    if save.lower() == 'yes':
        filename = input("Enter filename (e.g., performance.csv): ")
        df.to_csv(filename, index=False)
        print(f"✅ Data saved to {filename}")

if __name__ == "__main__":
    main()
