import pandas as pd
import matplotlib.pyplot as plt

def get_df(path: str) -> pd.DataFrame:
    df = pd.read_table(path, sep="\t")
    df.columns = ["Frequency", "Power", "Power in decibels"]
    return df

def show_power(df: pd.DataFrame, parametr: str) -> None:
    fig = plt.figure(figsize=(30, 5))
    if parametr == "Power":
        plt.ylabel("Мощность, Вт")
        plt.xlabel("Частота, Гц")
        plt.title('Спектр мощности в линейном масштабе')
        plt.plot(df["Frequency"], df[parametr], color='blue', linestyle='-', linewidth=2)
    elif parametr == "Power in decibels":
        plt.ylabel("Мощность, децибелах")
        plt.xlabel("Частота, Гц")
        plt.title('Спектр мощности в логарифмическом масштабе')
        plt.plot(df["Frequency"], df[parametr], color='orange', linestyle='-', linewidth=2)
    plt.show()


if __name__ =="__main__":
    show_power(get_df("samples/unipolar_signal_amplitude.txt"), "Power")
    show_power(get_df("samples/delta_function_choice_2.txt"), "Power in decibels")