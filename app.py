import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def create_data():
    # Simulated object detection data
    object_classes = ['Person', 'Bicycle', 'Car', 'Motorcycle', 'Airplane', 'Bus', 'Train', 'Truck', 'Boat',
                      'Traffic Light']
    frequencies = np.random.randint(10, 100, size=len(object_classes))
    return pd.DataFrame({'Object Class': object_classes, 'Frequency': frequencies})


def plot_data(df):
    # Plotting function
    plt.figure(figsize=(10, 6))
    plt.bar(df['Object Class'], df['Frequency'], color='skyblue')
    plt.xlabel('Object Class')
    plt.ylabel('Frequency')
    plt.title('Frequency of Object Classes Detected by YOLOv5')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt


def main():
    st.title("YOLOv5 Object Detection on COCO Dataset")

    df = create_data()

    # Display the plot
    st.header("Object Class Distribution")
    fig = plot_data(df)
    st.pyplot(fig)

    # Display a subset of data
    st.header("Data Subset")
    st.dataframe(df)


if __name__ == "__main__":
    main()
