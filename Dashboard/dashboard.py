import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import scipy as sp
from babel.numbers import format_currency

sns.set(style="dark")

# ! Create the helper functions needed to prepare various dataframes


# ! 1. create_daily_orders_df(df) to set up the daily_orders_df


def create_daily_orders_df(df):
    daily_orders_df = df.resample(rule="D", on="order_date").agg(
        {"order_id": "nunique", "total_price": "sum"}
    )
    daily_orders_df = daily_orders_df.reset_index()

    daily_orders_df.rename(
        columns={"order_id": "order_count", "total_price": "revenue"}, inplace=True
    )

    return daily_orders_df


# ! 2. create_sum_order_items_df(df) to set up the sum_order_items_df


def create_sum_order_items_df(df):
    sum_order_items_df = (
        df.groupby("product_name")
        .quantity_x.sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    return sum_order_items_df
