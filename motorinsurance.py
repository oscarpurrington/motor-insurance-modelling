from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt
full_motor_data = fetch_openml(data_id=43593, as_frame=True, parser="auto")
df = full_motor_data.frame

df = df.dropna()


def claims_per_exposure_vs_age():
    df["ClaimFreq"] = df["ClaimNb"] / df["Exposure"]

    grouped_age = (df.groupby("DrivAge")[["ClaimNb","Exposure"]].sum().reset_index())

    grouped_age["Freq"] = grouped_age["ClaimNb"]/grouped_age["Exposure"]

    plt.figure(figsize=(10,10))
    plt.xlabel("Age")
    plt.ylabel("Claims per Person-Year")
    plt.title("Claims vs Age")
    plt.plot(grouped_age["DrivAge"],grouped_age["Freq"], color='Red')
    plt.show()


def claims_per_VehPower_vs_age():
    df["ClaimFreq"] = df["ClaimNb"] / df["Exposure"]
    grouped_vehPower = (df.groupby("VehPower")[["ClaimNb","Exposure"]].sum().reset_index())
    grouped_vehPower["Freq"] = grouped_vehPower["ClaimNb"]/grouped_vehPower["Exposure"]

    plt.figure(figsize=(10,10))
    plt.xlabel("Vehicle Power")
    plt.ylabel("Claims per Person-Year")
    plt.title("Claims vs Vehicle Power")
    plt.bar(grouped_vehPower["VehPower"],grouped_vehPower["Freq"], color="Green")
    plt.show()

def main():
    choice = int(input("1. vs Age\n2. vs VehPower\n?: "))
    if choice == 1:
        claims_per_exposure_vs_age()
    elif choice == 2:
        claims_per_VehPower_vs_age()
    
main()
