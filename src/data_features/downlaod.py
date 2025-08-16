import polars as pl
import pandas as pd
import yfinance as yf

# ==== Download from yahoo finance ====
def download_data(index_name = str) -> pl.DataFrame:
    """
        Download Yahoo finance Data from the API
        Return a polars Dataframe
    """
    index = yf.download(index_name, start= "2015-01-01")
    df = pl.from_pandas(
    index, 
    include_index= True
    ).rename(
        {
            f"('Close', '{index_name}')" : "Close", 
            f"('High', '{index_name}')" : "High", 
            f"('Low', '{index_name}')" : "Low",
            f"('Open', '{index_name}')" : "Open",
            f"('Volume', '{index_name}')" : "Volume"
        }
    )
    return df

tesla = download_data(index_name="TSLA")
print(tesla)
