# BRAND DETECTION

- Showcasing an innovative Brand detection tool for urban environments

**Author:** Dhruv Raghav  
**Date:** 4/29/2024  
**Institution:** IUI  

## ABSTRACT

This report explores the application of the Deep Learning model You Only Look Once (YOLOv5) version 5, specifically designed for brand recognition using images collected from the web. We trained this model over 150 epochs, utilizing various datasets including 'Logo-2k+', 'Flickr-27', and additional images sourced from Google Maps. The model achieved an accuracy exceeding 95%. The performance of this model was compared with other object detection models such as ResNet, AlexNet, GoogLeNet, and MobileNet using the Mean Average Precision (mAP) metric. Our final results demonstrate significant improvement in effectively identifying logos, particularly in lower quality images. 
Along with this, we have created an API functionality for this model which makes it easier for this model to be integrated on any platform, plus a Streamlit application which helps in Batch Processing (Uploading multiple images).

## INTRODUCTION

In this modern era, numerous brands encounter the challenge of unauthorized duplication and use of their logos by smaller businesses. This situation can lead to several significant issues for the original brand, as they may face potential lawsuits if unforeseen circumstances arise due to their inaction against logo duplication. Addressing this challenge, we took up this project in which we detect logos from images and label them. 

We harness advanced Deep Learning models to enable real-time brand detection through logos. These models exhibit exceptional accuracy in logo detection, having been trained on a comprehensive dataset of over 9,500 images sourced from open platforms such as Kaggle and Wikipedia. Additionally, we supplemented our training data with images obtained from Google's Street View application.

This analysis not only underscores the importance of selecting appropriate deep learning architectures for specific tasks but also sheds light on the potential for optimizing brand detection systems for practical applications.
In this project, we trained five models to detect brands and identify logos and compared their performance. This project contains the following models:
- ResNet
- AlexNet
- MobileNet
- GoogLeNet
- Yolov5
The goal here is to determine what models are the best performing for images of low/blurred quality. For model evaluation, we use the Mean Average Precision metric.

### Problem Description

In today's competitive business landscape, the unauthorized duplication and misuse of brand logos by smaller companies pose a significant challenge for established brands. This unlawful practice can expose brands to potential legal liabilities if they fail to take appropriate action against such infringements. To address this pressing issue, we have undertaken a project aimed at detecting and labeling logos from images using advanced deep learning techniques.
Traditional Logo Detection Methods: Traditional Logo detection models were trained on images of better quality and the logo occupied a lot of space in the image. These models when used to detect logos on images of lower pixel values or images where the logo does not occupy the majority portion of the image perform poorly.
The Need for Advanced Logo Detection Systems: With a growing number of small businesses the chances of a brand’s logo which is its identity being duplicated is high, also a brand can analyze a street’s information with the help the brands present on that particular street and make strategies accordingly. The advanced Logo detection models are capable of getting these things done.

## DATA DESCRIPTION

The data for this project was sourced from three distinct repositories. Firstly, we utilized the Logo-2k+ dataset, a comprehensive collection designed for scalable logo classification tasks. This dataset features over 2,000 images spanning 10 root categories, encompassing a diverse array of real-world logo classes.
[Logo-2k+ Link](https://your-link-here.com)

Secondly, we integrated the 'Flickr Logos 27' dataset, sourced from annotated logos extracted from Flickr. This dataset comprises more than 4,000 images in total and encompasses 27 annotated classes.
[Flickr Logos 27 Link](http://image.ntua.gr/iva/datasets/flickr_logos/)

Additionally, we curated a set of images from Google's Street View, which were subsequently manually annotated using the VGG Annotator tool. This dataset predominantly comprises images of lower quality, reflecting real-world scenarios where logo recognition remains challenging. For a glimpse into some of the images we collected, please refer to the below provided link.
[Test images Link](https://your-link-here.com)

## METHODOLOGY

- Data Collection
- Data Annotation (Labeling)
- Data Pre-processing
- Loading Data to data loader
- Adjusting model hyperparameters
- Finding accuracy
- Testing on low quality images

## RESULTS

After training and testing the models, we have obtained the following results:

| Model Name | Mean Average Precision (%) |
|------------|----------------------------|
| ResNet     | 69                         |
| AlexNet    | 74                         |
| GoogLeNet  | 10                         |
| MobileNet  | 23                         |
| YOLOv5     | >95                        |

### Here is performance details of the YOLOv5 model:
## REFERENCES

- [YOLOv5 model implementation](https://github.com/ultralytics/yolov5/releases)
- Szeliski, R. (2010). Computer Vision: Algorithms and Applications. Springer.: [Link](https://link.springer.com/book/10.1007/978-1-84882-935-0)
- He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep Residual Learning for Image Recognition. Journal of Machine Learning Research, 15(1), 770-778. : [Link](https://arxiv.org/abs/1512.03385)
- Redmon, J. (2018, April 8). YOLOv3: An Incremental Improvement. YOLO. [Link](https://pjreddie.com/darknet/yolo/)
- Ren, S., He, K., Girshick, R., & Sun, J. (2015). Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks. In Proceedings of the Neural Information Processing Systems (pp. 91-99). MIT Press.: [Link](https://arxiv.org/abs/1506.01497)
- For Dataset: [Flickr Logos Dataset](http://image.ntua.gr/iva/datasets/flickr_logos/)

## APPENDICES

### Appendix 1: Contributions from Each Member

- Data collection and model development: Dhruv Raghav and Ankita Shelke
- Web application and API functionality implementation: Sumedh and Bhushan
- Report: Dhruv Raghav and Bhushan Shelke
- PPT Slides: Ankita Shelke and Sumedh Sonawane
- Demo Presentation:  Dhruv Raghav, Bhushan Shelke, Ankita Shelke and Sumedh Sonawane


