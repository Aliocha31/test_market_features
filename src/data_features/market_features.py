#%%
import polars as pl 
from downlaod import download_data

tesla = download_data(index_name="TSLA")
mc =  download_data(index_name="MC.PA")
open = download_data(index_name="OPEN")
nvdia = download_data(index_name="NVDA")


# %%

def market_feat(df : pl.DataFrame) -> pl.DataFrame : 

    """
        ==== Rendements ====
        Calcul du log des rendements  : rt = ln(Pt/Pt-1) <=> rt = ln(Pt) - ln(Pt-1)

        ==== Rolling Volatility / Volatilité Glissante ====
        Calcul de la variable mobile : 

        ==== Moyenne Mobile ====
        Calcul de la moyenne mobile : Simple Moving Average (SMA)
    """
    window = 5
    df_returns = df.with_columns(
        (pl.col("Close") / pl.col("Close").shift(1)).log().alias("Return (log)") #calcul des rendements
        ).with_columns( 
        pl.col("Return (log)").rolling_std(window).alias("Rolling Volatility") #volatalité glissante
        )
    return df_returns

df_tesla = market_feat(tesla)
print(df_tesla)


# %%
