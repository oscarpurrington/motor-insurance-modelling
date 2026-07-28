from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt
import seaborn as sns
full_motor_data = fetch_openml(data_id=43593, as_frame=True, parser="auto")
df = full_motor_data.frame

df = df.dropna()

features = list(df.columns.values)
del features[0:2]


def plot_claim_frequency(df, feature):
    df["ClaimFreq"] = df["ClaimNb"] / df["Exposure"]
    
    grouped_feature = (df.groupby(feature)[["ClaimNb","Exposure"]].sum().reset_index())
    
    grouped_feature["Freq"] = grouped_feature["ClaimNb"]/grouped_feature["Exposure"]


    
    plt.figure(figsize=(10,10))
    plt.xlabel(f"{feature}")
    plt.ylabel("Claims per Person-Year")
    plt.title(f"Claims vs {feature}")
    plt.plot(grouped_feature[feature],grouped_feature["Freq"], color='Red')
    plt.show()


for feature in features:
    plot_claim_frequency(df, feature)


def correlation_matrix(df):

    numerical_df = df.select_dtypes(include=["number"])
    matrix = numerical_df.corr()
    plt.figure(figsize=(10,10))
    sns.heatmap(matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

correlation_matrix(df)

