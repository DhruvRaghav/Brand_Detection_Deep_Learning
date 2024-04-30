import skimage.io as io
from face_2D_detect import *
import blur
import time
from face_2D_detect_blur import *
from face_2D_detect_1 import *
from face_2D_detect_blur_1 import *
import streamlit as st
# Set page config
st.set_page_config(
    page_title="BRAND DETECTION",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="expanded",
)
# Custom CSS for styling
st.markdown("""
<style>
    /* Title styling */
    .css-1y0tads {
        font-size: 3rem; /* Adjust the size as needed */
        font-weight: bold;
        color: #FF6347; /* Change color as desired */
        text-align: center;
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }
    /* Background color of main page */
    body {
        background-color: #F5F5F5; /* Light grey background, adjust as needed */
    }
    /* Sidebar styling */
    .css-1lcbmhc {
        background-color: #f0f0f0; /* Adjust sidebar background color */
        color: #333333; /* Adjust text color */
    }
    /* Sidebar header style */
    .css-hi6a2p {
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("BRAND DETECTION")
os.makedirs('API_DATA/brand_box', exist_ok=True)
os.makedirs('API_DATA/brand_blur', exist_ok=True)
os.makedirs('API_DATA/brand_draw', exist_ok=True)



def delete_image(file_path):
    try:
        os.remove(file_path)
        st.success(f"Image {file_path} deleted successfully!")
    except Exception as e:
        st.error(f"Error deleting image: {e}")


def process_pothole_image(option, files):
    if files is not None:
        for file in files:
            img = io.imread(file)
            # Save the uploaded image
            save_path = f'API_DATA/{option}/{file.name}'
            io.imsave(save_path, img)

            # Display Image Statistics
            st.subheader("Image Statistics")
            st.write(f"Dimensions: {img.shape[0]} x {img.shape[1]}")
            st.write(f"Channels: {img.shape[2]}")

            # # Display the uploaded image
            # st.subheader("Uploaded Image")
            # st.image(img, caption="Original Image", use_column_width=True)

            # Progress Bar
            progress_bar = st.progress(0)

            # Loading Spinner
            with st.spinner(f"Processing {file.name}..."):
                for i in range(1, 101):
                    time.sleep(0.05)
                    progress_bar.progress(i)

            # Processing Time
            st.subheader("Processing Time")
            st.write(f"Time taken: {time.process_time()} seconds")

            # Display Original vs Processed Images Side-by-Side
            col1, col2 = st.columns(2)
            col1.subheader("Original Image")
            col1.image(img, caption="Original Image", use_column_width=True)

            col2.subheader("Processed Image")
            # Result Container
            result_container = col2.empty()

            if option in ['pothole_box']:
                print("okay hi")
                result = run5(source=f'API_DATA/{option}/{file.name}', nosave=True, box=True, device='cpu')
                st.json(result)
            elif option in ['pothole_blur']:
                result = run6(source=f'API_DATA/{option}/{file.name}', nosave=True, box=True, device='cpu')
                blur.rectblur_NEW(f'API_DATA/{option}/{file.name}', result, option,file.name)
                result_image_path = f'API_DATA/{option}/{file.name}'
                result_image = io.imread(result_image_path)
                result_container.image(result_image, caption="Result", use_column_width=True)

                # Delete the processed image
                delete_image(result_image_path)

            elif option in ['pothole_draw']:
                result_path = run5(source=f'API_DATA/{option}/{file.name}', nosave=True, img=True, device='cpu',save_dir=f'C:/dataset/object_detection-main/API_DATA/{option}/{file.name}')
                result_image = io.imread(result_path)
                result_container.image(result_image, caption="Result with Bounding Boxes", use_column_width=True)

                # Delete the processed image
                delete_image(result_path)


            # elif option in ['Pothole_label']:
            #     result_path = run4(source=f'API_DATA/{option}/{file.name}', nosave=True,  device='cpu')
            #     result_image = io.imread(result_path)
            #     result_container.image(result_image, caption="Result with Bounding Boxes", use_column_width=True)





                # Delete the processed image
                # delete_image(result_path)



def process_object_image(option, files):
    if files is not None:
        for file in files:
            img = io.imread(file)
            print("1")
            # Save the uploaded image
            save_path = f'API_DATA/{option}/{file.name}'
            io.imsave(save_path, img)
            print("2")
            # Display Image Statistics
            st.subheader("Image Statistics")
            st.write(f"Dimensions: {img.shape[0]} x {img.shape[1]}")
            st.write(f"Channels: {img.shape[2]}")
            print("3")
            # # Display the uploaded image
            # st.subheader("Uploaded Image")
            # st.image(img, caption="Original Image", use_column_width=True)

            # Progress Bar
            progress_bar = st.progress(0)
            print("4")
            # Loading Spinner
            with st.spinner(f"Processing {file.name}..."):
                for i in range(1, 101):
                    time.sleep(0.05)
                    progress_bar.progress(i)

            # Processing Time
            st.subheader("Processing Time")
            st.write(f"Time taken: {time.process_time()} seconds")

            # Display Original vs Processed Images Side-by-Side
            col1, col2 = st.columns(2)
            col1.subheader("Original Image")
            col1.image(img, caption="Original Image", use_column_width=True)

            col2.subheader("Processed Image")
            # Result Container
            result_container = col2.empty()

            if option in ['object_box']:

                result = run2(source=f'API_DATA/{option}/{file.name}', nosave=True, box=True, device='cpu')
                st.json(result)


            elif option in ['object_blur']:

                result = run(source=f'API_DATA/{option}{file.name}', nosave=True, box=True, device='cpu')
                blur.rectblur_NEW(f'API_DATA/{option}/{file.name}', result, option, file.name)
                result_image_path = f'API_DATA/{option}/{file.name}'
                result_image = io.imread(result_image_path)
                result_container.image(result_image, caption="Result", use_column_width=True)
                print("5")
                # Delete the processed image
                delete_image(result_image_path)

            elif option in ['object_draw']:
                print("6")
                result_path = run2(source=f'API_DATA/{option}/{file.name}', nosave=True, img=True, device='cpu',
                                   save_dir=f'API_DATA/{option}/{file.name}')
                result_image = io.imread(result_path)
                result_container.image(result_image, caption="Result with Bounding Boxes", use_column_width=True)

                # Delete the processed image
                delete_image(result_path)







def process_brand_image(option, files):
    if files is not None:
        for file in files:
            img = io.imread(file)
            print("1")
            # Save the uploaded image
            save_path = f'API_DATA/{option}/{file.name}'
            io.imsave(save_path, img)
            print("2")
            # Display Image Statistics
            st.subheader("Image Statistics")
            st.write(f"Dimensions: {img.shape[0]} x {img.shape[1]}")
            st.write(f"Channels: {img.shape[2]}")
            print("3")
            # # Display the uploaded image
            # st.subheader("Uploaded Image")
            # st.image(img, caption="Original Image", use_column_width=True)

            # Progress Bar
            progress_bar = st.progress(0)
            print("4")
            # Loading Spinner
            with st.spinner(f"Processing {file.name}..."):
                for i in range(1, 101):
                    time.sleep(0.05)
                    progress_bar.progress(i)

            # Processing Time
            st.subheader("Processing Time")
            st.write(f"Time taken: {time.process_time()} seconds")

            # Display Original vs Processed Images Side-by-Side
            col1, col2 = st.columns(2)
            col1.subheader("Original Image")
            col1.image(img, caption="Original Image", use_column_width=True)

            col2.subheader("Processed Image")
            # Result Container
            result_container = col2.empty()

            if option in ['brand_box']:

                result = run02(source=f'API_DATA/{option}/{file.name}', nosave=True, box=True, device='cpu')
                st.json(result)


            elif option in ['brand_blur']:

                result = run00(source=f'API_DATA/{option}/{file.name}', nosave=True, box=True, device='cpu')
                blur.rectblur_NEW(f'API_DATA/{option}/{file.name}', result, option, file.name)
                result_image_path = f'API_DATA/{option}/{file.name}'
                result_image = io.imread(result_image_path)
                result_container.image(result_image, caption="Result", use_column_width=True)
                print("5")
                # Delete the processed image
                delete_image(result_image_path)

            elif option in ['brand_draw']:
                print("6")
                result_path = run02(source=f'API_DATA/{option}/{file.name}', nosave=True, img=True, device='cpu',
                                   save_dir=f'API_DATA/{option}/{file.name}')
                result_image = io.imread(result_path)
                result_container.image(result_image, caption="Result with Bounding Boxes", use_column_width=True)

                # Delete the processed image
                delete_image(result_path)





def process_solar_image(option, files):
    if files is not None:
        for file in files:
            img = io.imread(file)
            print("1")
            # Save the uploaded image
            save_path = f'API_DATA/{option}/{file.name}'
            io.imsave(save_path, img)
            print("2")
            # Display Image Statistics
            st.subheader("Image Statistics")
            st.write(f"Dimensions: {img.shape[0]} x {img.shape[1]}")
            st.write(f"Channels: {img.shape[2]}")
            print("3")
            # # Display the uploaded image
            # st.subheader("Uploaded Image")
            # st.image(img, caption="Original Image", use_column_width=True)

            # Progress Bar
            progress_bar = st.progress(0)
            print("4")
            # Loading Spinner
            with st.spinner(f"Processing {file.name}..."):
                for i in range(1, 101):
                    time.sleep(0.05)
                    progress_bar.progress(i)

            # Processing Time
            st.subheader("Processing Time")
            st.write(f"Time taken: {time.process_time()} seconds")

            # Display Original vs Processed Images Side-by-Side
            col1, col2 = st.columns(2)
            col1.subheader("Original Image")
            col1.image(img, caption="Original Image", use_column_width=True)

            col2.subheader("Processed Image")
            # Result Container
            result_container = col2.empty()

            if option in ['solar_box']:

                result = run002(source=f'API_DATA/{option}/{file.name}', nosave=True, box=True, device='cpu')
                st.json(result)


            elif option in ['solar_blur']:

                result = run1000(source=f'API_DATA/{option}/{file.name}', nosave=True, box=True, device='cpu')
                blur.rectblur_NEW(f'API_DATA/{option}/{file.name}', result, option, file.name)
                result_image_path = f'API_DATA/{option}/{file.name}'
                result_image = io.imread(result_image_path)
                result_container.image(result_image, caption="Result", use_column_width=True)
                print("5")
                # Delete the processed image
                delete_image(result_image_path)

            elif option in ['solar_draw']:
                print("6")
                result_path = run002(source=f'API_DATA/{option}/{file.name}', nosave=True, img=True, device='cpu',
                                   save_dir=f'API_DATA/{option}/{file.name}')
                result_image = io.imread(result_path)
                result_container.image(result_image, caption="Result with Bounding Boxes", use_column_width=True)

                # Delete the processed image
                delete_image(result_path)




def process_face2d_image(option, files):
    if files is not None:
        for file in files:
            img = io.imread(file)
            print("1")
            # Save the uploaded image
            save_path = f'API_DATA/{option}/{file.name}'
            io.imsave(save_path, img)
            print("2")
            # Display Image Statistics
            st.subheader("Image Statistics")
            st.write(f"Dimensions: {img.shape[0]} x {img.shape[1]}")
            st.write(f"Channels: {img.shape[2]}")
            print("3")
            # # Display the uploaded image
            # st.subheader("Uploaded Image")
            # st.image(img, caption="Original Image", use_column_width=True)

            # Progress Bar
            progress_bar = st.progress(0)
            print("4")
            # Loading Spinner
            with st.spinner(f"Processing {file.name}..."):
                for i in range(1, 101):
                    time.sleep(0.05)
                    progress_bar.progress(i)

            # Processing Time
            st.subheader("Processing Time")
            st.write(f"Time taken: {time.process_time()} seconds")

            # Display Original vs Processed Images Side-by-Side
            col1, col2 = st.columns(2)
            col1.subheader("Original Image")
            col1.image(img, caption="Original Image", use_column_width=True)

            col2.subheader("Processed Image")
            # Result Container
            result_container = col2.empty()

            if option in ['face2d_box']:

                result = run0002(source=f'API_DATA/{option}/{file.name}', nosave=True, box=True, device='cpu')
                st.json(result)


            elif option in ['face2d_blur']:

                result = run000(source=f'API_DATA/{option}/{file.name}', nosave=True, box=True, device='cpu')
                blur.rectblur_NEW(f'API_DATA/{option}/{file.name}', result, option, file.name)
                result_image_path = f'API_DATA/{option}/{file.name}'
                result_image = io.imread(result_image_path)
                result_container.image(result_image, caption="Result", use_column_width=True)
                print("5")
                # Delete the processed image
                delete_image(result_image_path)

            elif option in ['face2d_draw']:
                print("6")
                result_path = run0002(source=f'API_DATA/{option}/{file.name}', nosave=True, img=True, device='cpu',
                                   save_dir=f'API_DATA/{option}/{file.name}')
                result_image = io.imread(result_path)
                result_container.image(result_image, caption="Result with Bounding Boxes", use_column_width=True)

                # Delete the processed image
                delete_image(result_path)





def process_face360_image(option, files):
    if files is not None:
        for file in files:
            img = io.imread(file)
            print("1")
            # Save the uploaded image
            save_path = f'API_DATA/{option}/{file.name}'
            io.imsave(save_path, img)
            print("2")
            # Display Image Statistics
            st.subheader("Image Statistics")
            st.write(f"Dimensions: {img.shape[0]} x {img.shape[1]}")
            st.write(f"Channels: {img.shape[2]}")
            print("3")
            # # Display the uploaded image
            # st.subheader("Uploaded Image")
            # st.image(img, caption="Original Image", use_column_width=True)

            # Progress Bar
            progress_bar = st.progress(0)
            print("4")
            # Loading Spinner
            with st.spinner(f"Processing {file.name}..."):
                for i in range(1, 101):
                    time.sleep(0.05)
                    progress_bar.progress(i)

            # Processing Time
            st.subheader("Processing Time")
            st.write(f"Time taken: {time.process_time()} seconds")

            # Display Original vs Processed Images Side-by-Side
            col1, col2 = st.columns(2)
            col1.subheader("Original Image")
            col1.image(img, caption="Original Image", use_column_width=True)

            col2.subheader("Processed Image")
            # Result Container
            result_container = col2.empty()

            if option in ['face360_box']:

                result = run00002(source=f'API_DATA/{option}/{file.name}', nosave=True, box=True, device='cpu')
                st.json(result)


            elif option in ['face360_blur']:

                result = run0000(source=f'API_DATA/{option}/{file.name}', nosave=True, box=True, device='cpu')
                blur.rectblur_NEW(f'API_DATA/{option}/{file.name}', result, option, file.name)
                result_image_path = f'API_DATA/{option}/{file.name}'
                result_image = io.imread(result_image_path)
                result_container.image(result_image, caption="Result", use_column_width=True)
                print("5")
                # Delete the processed image
                delete_image(result_image_path)

            elif option in ['face360_draw']:
                print("6")
                result_path = run00002(source=f'API_DATA/{option}/{file.name}', nosave=True, img=True, device='cpu',
                                   save_dir=f'API_DATA/{option}/{file.name}')
                result_image = io.imread(result_path)
                result_container.image(result_image, caption="Result with Bounding Boxes", use_column_width=True)

                # Delete the processed image
                delete_image(result_path)



def process_lp_2p_image(option, files):
    if files is not None:
        for file in files:
            img = io.imread(file)
            print("1")
            # Save the uploaded image
            save_path = f'API_DATA/{option}/{file.name}'
            io.imsave(save_path, img)
            print("2")
            # Display Image Statistics
            st.subheader("Image Statistics")
            st.write(f"Dimensions: {img.shape[0]} x {img.shape[1]}")
            st.write(f"Channels: {img.shape[2]}")
            print("3")
            # # Display the uploaded image
            # st.subheader("Uploaded Image")
            # st.image(img, caption="Original Image", use_column_width=True)

            # Progress Bar
            progress_bar = st.progress(0)
            print("4")
            # Loading Spinner
            with st.spinner(f"Processing {file.name}..."):
                for i in range(1, 101):
                    time.sleep(0.05)
                    progress_bar.progress(i)

            # Processing Time
            st.subheader("Processing Time")
            st.write(f"Time taken: {time.process_time()} seconds")

            # Display Original vs Processed Images Side-by-Side
            col1, col2 = st.columns(2)
            col1.subheader("Original Image")
            col1.image(img, caption="Original Image", use_column_width=True)

            col2.subheader("Processed Image")
            # Result Container
            result_container = col2.empty()

            if option in ['lp_2d_box']:

                result = run000002(source=f'API_DATA/{option}/{file.name}', nosave=True, box=True, device='cpu')
                st.json(result)


            elif option in ['lp_2d_blur']:

                result = run00010(source=f'API_DATA/{option}/{file.name}', nosave=True, box=True, device='cpu')
                blur.rectblur_NEW(f'API_DATA/{option}/{file.name}', result, option, file.name)
                result_image_path = f'API_DATA/{option}/{file.name}'
                result_image = io.imread(result_image_path)
                result_container.image(result_image, caption="Result", use_column_width=True)
                print("5")
                # Delete the processed image
                delete_image(result_image_path)

            elif option in ['lp_2d_draw']:
                print("6")
                result_path = run000002(source=f'API_DATA/{option}/{file.name}', nosave=True, img=True, device='cpu',
                                   save_dir=f'API_DATA/{option}/{file.name}')
                result_image = io.imread(result_path)
                result_container.image(result_image, caption="Result with Bounding Boxes", use_column_width=True)

                # Delete the processed image
                delete_image(result_path)


def process_tsdr_image(option, files):
    if files is not None:
        for file in files:
            img = io.imread(file)
            print("1")
            # Save the uploaded image
            save_path = f'API_DATA/{option}/{file.name}'
            io.imsave(save_path, img)
            print("2")
            # Display Image Statistics
            st.subheader("Image Statistics")
            st.write(f"Dimensions: {img.shape[0]} x {img.shape[1]}")
            st.write(f"Channels: {img.shape[2]}")
            print("3")
            # # Display the uploaded image
            # st.subheader("Uploaded Image")
            # st.image(img, caption="Original Image", use_column_width=True)

            # Progress Bar
            progress_bar = st.progress(0)
            print("4")
            # Loading Spinner
            with st.spinner(f"Processing {file.name}..."):
                for i in range(1, 101):
                    time.sleep(0.05)
                    progress_bar.progress(i)

            # Processing Time
            st.subheader("Processing Time")
            st.write(f"Time taken: {time.process_time()} seconds")

            # Display Original vs Processed Images Side-by-Side
            col1, col2 = st.columns(2)
            col1.subheader("Original Image")
            col1.image(img, caption="Original Image", use_column_width=True)

            col2.subheader("Processed Image")
            # Result Container
            result_container = col2.empty()

            if option in ['tsdr_box']:

                result = run0000002(source=f'API_DATA/{option}/{file.name}', nosave=True, box=True, device='cpu')
                st.json(result)


            elif option in ['tsdr_blur']:

                result = run00000(source=f'API_DATA/{option}/{file.name}', nosave=True, box=True, device='cpu')
                blur.rectblur_NEW(f'API_DATA/{option}/{file.name}', result, option, file.name)
                result_image_path = f'API_DATA/{option}/{file.name}'
                result_image = io.imread(result_image_path)
                result_container.image(result_image, caption="Result", use_column_width=True)
                print("5")
                # Delete the processed image
                delete_image(result_image_path)

            elif option in ['tsdr_draw']:
                print("6")
                result_path = run0000002(source=f'API_DATA/{option}/{file.name}', nosave=True, img=True, device='cpu',
                                   save_dir=f'API_DATA/{option}/{file.name}')
                result_image = io.imread(result_path)
                result_container.image(result_image, caption="Result with Bounding Boxes", use_column_width=True)

                # Delete the processed image
                delete_image(result_path)


def main():
    import streamlit.components.v1 as components

    st.sidebar.header("Choose an option")



    # Create a dropdown for brand options

    Brand_option = st.sidebar.selectbox("Brand Detection Options", ["Select an option", "Brand Box", "Brand Blur", "Brand Draw"])

    files = st.file_uploader("Upload Images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    if st.button("Process"):


        if Brand_option != "Select an option":
            print("0")
            process_brand_image(Brand_option.lower().replace(" ", "_"), files)
            print("finished")







if __name__ == "__main__":
    main()
