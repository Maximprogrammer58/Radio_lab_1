import pandas as pd
import matplotlib.pyplot as plt

def get_df(path: str) -> pd.DataFrame:
    df = pd.read_table(path, sep="\t")
    df.columns = ["Frequency", "Signals", "P", "Inv", "Number"]
    return df

def show_signal(df: pd.DataFrame) -> None:
    fig = plt.figure(figsize=(30, 5))
    plt.ylabel("Амплитуда, В")
    plt.xlabel("Частота, Гц")
    plt.plot(df["Frequency"], df["Singals"], color='green', linestyle='-', linewidth=2)
    plt.show()
    
def show_spectr(df: pd.DataFrame) -> None:
    fig = plt.figure(figsize=(30, 5))
    plt.ylabel("Амплитуда, В")
    plt.xlabel("Частота, Гц")
    plt.plot(df["Frequency"], df["P"], color='green', linestyle='-', linewidth=2)
    plt.show()


if __name__ == "__main__":
    show_signal(get_df(r"samples2/AM_1.txt"))
    show_spectr(get_df(r"samples2/AM_1.txt"))