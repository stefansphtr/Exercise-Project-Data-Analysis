import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import scipy as sp
from babel.numbers import format_currency

sns.set(style="dark")

# ! Create the helper functions needed to prepare various dataframes


# ! 1. create_daily_orders_df() to set up the daily_orders_df


def create_daily_orders_df(df):
    daily_orders_df = df.resample(rule="D", on="order_date").agg(
        {"order_id": "nunique", "total_price": "sum"}
    )
    daily_orders_df = daily_orders_df.reset_index()

    daily_orders_df.rename(
        columns={"order_id": "order_count", "total_price": "revenue"}, inplace=True
    )

    return daily_orders_df


# ! 2. create_sum_order_items_df() to set up the sum_order_items_df


def create_sum_order_items_df(df):
    sum_order_items_df = (
        df.groupby("product_name")
        .quantity_x.sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    return sum_order_items_df


# ! 3. create_bygender_df(df) to setup the bygender_df


def create_bygender_df(df):
    bygender_df = df.groupby(by="gender").customer_id.nunique().reset_index()
    bygender_df.rename(columns={"customer_id": "customer_count"}, inplace=True)

    return bygender_df


# ! 4. create_byage_df() to setup helper function of the byage_df


def create_byage_df(df):
    byage_df = df.groupby(by="age_group").customer_id.nunique().reset_index()
    byage_df.rename(columns={"customer_id": "customer_count"}, inplace=True)
    byage_df["age_group"] = pd.Categorical(
        byage_df["age_group"], ["Youth", "Adults", "Seniors"]
    )

    return byage_df
