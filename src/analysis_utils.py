import pandas as pd

def calculate_batting_strike_rate(runs, balls_faced):
    """Calculates batting strike rate."""
    return (runs / balls_faced) * 100 if balls_faced > 0 else 0

def calculate_bowling_economy(runs_conceded, overs_bowled):
    """Calculates bowling economy rate."""
    return runs_conceded / overs_bowled if overs_bowled > 0 else 0

def get_top_performers(df, metric, top_n=10, ascending=False):
    """
    Gets top N performers based on a given metric.
    Args:
        df (pd.DataFrame): DataFrame containing player stats.
        metric (str): The column name to rank by (e.g., 'runs', 'wickets').
        top_n (int): Number of top performers to return.
        ascending (bool): True for lowest values first, False for highest values first.
    Returns:
        pd.Series: Top performers.
    """
    if metric not in df.columns:
        return pd.Series(dtype='float64') # Return empty series if metric not found
    return df.groupby('player')[metric].sum().nlargest(top_n) if not ascending else df.groupby('player')[metric].sum().nsmallest(top_n)

def calculate_toss_advantage(matches_df):
    """
    Calculates the winning percentage for teams winning the toss.
    Args:
        matches_df (pd.DataFrame): DataFrame with match results.
    Returns:
        float: Percentage of matches won by toss-winning team.
    """
    toss_wins = matches_df[matches_df['toss_winner'] == matches_df['winner']]
    return (len(toss_wins) / len(matches_df)) * 100 if len(matches_df) > 0 else 0