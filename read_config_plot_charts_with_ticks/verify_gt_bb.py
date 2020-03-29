import os
import cv2
import json
import sys
import random

r'''
This is a function, you could simply write a loop to looping all the file within the images and gt folder.
Requirement:
- file_name should be without extension, and the paired image and gt have same file name
- img is png, gt is json

You could modified the verify function slightly to fit your json structure.
'''


def verify(images_file_name, gts_file_name):
    gt_dic = json.load(open(gts_file_name+".json",'r'))
    img =cv2.imread(images_file_name+".png")
    BGR = (0,255,0);

    #plot bounding box of plot
    plot_bb = gt_dic["PLOT_BB"];
    x0 = plot_bb["X0"]
    y0 = plot_bb["Y0"]
    width = plot_bb["WIDTH"]
    height = plot_bb["HEIGHT"]
    BGR = (100,100,100);
    drawrectangle(img, x0,y0,width,height,BGR, plot_bb)


    if("LABEL_BLOCKS"  in gt_dic["X_AXIS"]):
        for label_bb in gt_dic["X_AXIS"]["LABEL_BLOCKS"]:
            x0 = label_bb["BB"]["X0"]
            y0 = label_bb["BB"]["Y0"]
            width = label_bb["BB"]["WIDTH"]
            height = label_bb["BB"]["HEIGHT"]
            BGR = (255,0,0);
            # if(label_bb["TEXT"]!=""):
            drawrectangle(img, x0,y0,width,height,BGR,plot_bb)

    if("LABEL_BLOCKS"  in gt_dic["Y_AXIS"]):
        for label_bb in gt_dic["Y_AXIS"]["LABEL_BLOCKS"]:
            x0 = label_bb["BB"]["X0"]
            y0 = label_bb["BB"]["Y0"]
            width = label_bb["BB"]["WIDTH"]
            height = label_bb["BB"]["HEIGHT"]
            BGR = (255,0,0);
            # if(label_bb["TEXT"]!=""):
            drawrectangle(img, x0,y0,width,height,BGR,plot_bb)

    if("TICK_BLOCKS" in gt_dic["X_AXIS"]):
        for tick_bb in gt_dic["X_AXIS"]["TICK_BLOCKS"]:
            # x0 = tick_bb["BB"]["X0"]
            # y0 = tick_bb["BB"]["Y0"]
            # width = tick_bb["BB"]["WIDTH"]
            # height = tick_bb["BB"]["HEIGHT"]
            x0 = tick_bb["BB"]["X"]-5
            y0 = tick_bb["BB"]["Y"]-5
            width = tick_bb["BB"]["X"]+5
            height = tick_bb["BB"]["Y"]+5
            BGR = (0,0,255);
            drawrectangle(img, x0,y0,width,height,BGR,plot_bb)

    if("TICK_BLOCKS" in gt_dic["Y_AXIS"]):
        for tick_bb in gt_dic["Y_AXIS"]["TICK_BLOCKS"]:
            # x0 = tick_bb["BB"]["X0"]
            # y0 = tick_bb["BB"]["Y0"]
            # width = tick_bb["BB"]["WIDTH"]
            # height = tick_bb["BB"]["HEIGHT"]
            x0 = tick_bb["BB"]["X"]-5
            y0 = tick_bb["BB"]["Y"]-5
            width = tick_bb["BB"]["X"]+5
            height = tick_bb["BB"]["Y"]+5
            BGR = (0,0,255);
            drawrectangle(img, x0,y0,width,height,BGR,plot_bb)

    if("MAJOR_TICK_LABELS"  in gt_dic["X_AXIS"]):
        for major_tick_bb in gt_dic["X_AXIS"]["MAJOR_TICK_LABELS"]:
            x0 = major_tick_bb["BB"]["X0"]
            y0 = major_tick_bb["BB"]["Y0"]
            width = major_tick_bb["BB"]["WIDTH"]
            height = major_tick_bb["BB"]["HEIGHT"]
            BGR = (0,255,255);
            # if(major_tick_bb['TEXT']!=""):
            drawrectangle(img, x0,y0,width,height,BGR,plot_bb)

    if("MAJOR_TICK_LABELS"  in gt_dic["Y_AXIS"]):
        for major_tick_bb in gt_dic["Y_AXIS"]["MAJOR_TICK_LABELS"]:
            x0 = major_tick_bb["BB"]["X0"]
            y0 = major_tick_bb["BB"]["Y0"]
            width = major_tick_bb["BB"]["WIDTH"]
            height = major_tick_bb["BB"]["HEIGHT"]
            BGR = (0,255,255);
            # if(major_tick_bb["TEXT"]!=""):
            drawrectangle(img, x0,y0,width,height,BGR,plot_bb)

    if("MINOR_TICK_LABELS"  in gt_dic["X_AXIS"]):
        for minor_tick_bb in gt_dic["X_AXIS"]["MINOR_TICK_LABELS"]:
            x0 = minor_tick_bb["BB"]["X0"]
            y0 = minor_tick_bb["BB"]["Y0"]
            width = minor_tick_bb["BB"]["WIDTH"]
            height = minor_tick_bb["BB"]["HEIGHT"]
            BGR = (255,255,0);
            # if(minor_tick_bb["TEXT"]!=""):
            drawrectangle(img, x0,y0,width,height,BGR,plot_bb)

    if("MINOR_TICK_LABELS"  in gt_dic["Y_AXIS"]):
        for minor_tick_bb in gt_dic["Y_AXIS"]["MINOR_TICK_LABELS"]:
            x0 = minor_tick_bb["BB"]["X0"]
            y0 = minor_tick_bb["BB"]["Y0"]
            width = minor_tick_bb["BB"]["WIDTH"]
            height = minor_tick_bb["BB"]["HEIGHT"]
            BGR = (255,255,0);
            # if(minor_tick_bb["TEXT"]!=""):
            drawrectangle(img, x0,y0,width,height,BGR,plot_bb)


    x_axis_label_bb = gt_dic["X_AXIS"]["X_AXIS_LABEL"];
    x0 = x_axis_label_bb["BB"]["X0"]
    y0 = x_axis_label_bb["BB"]["Y0"]
    width = x_axis_label_bb["BB"]["WIDTH"]
    height = x_axis_label_bb["BB"]["HEIGHT"]
    BGR = (100,255,0);
    drawrectangle(img, x0,y0,width,height,BGR,plot_bb)

    y_axis_label_bb = gt_dic["Y_AXIS"]["Y_AXIS_LABEL"];
    x0 = y_axis_label_bb["BB"]["X0"]
    y0 = y_axis_label_bb["BB"]["Y0"]
    width = y_axis_label_bb["BB"]["WIDTH"]
    height = y_axis_label_bb["BB"]["HEIGHT"]
    BGR = (100,255,0);
    drawrectangle(img, x0,y0,width,height,BGR,plot_bb)

    title_bb = gt_dic["TITLE"];
    x0 = title_bb["BB"]["X0"]
    y0 = title_bb["BB"]["Y0"]
    width = title_bb["BB"]["WIDTH"]
    height = title_bb["BB"]["HEIGHT"]
    BGR = (20,100,20);
    drawrectangle(img, x0,y0,width,height,BGR,plot_bb)



    #
    # for axis in gt_dic["input"]["task4_output"]["axes"]:
    #     ## If you have multiple keys here, e.g., axes type, add an if judgement here
    #     ## to only process the key items which include tick points coords.
    #     for item in gt_dic["input"]["task4_output"]["axes"][axis]:
    #         x0 = item["tick_pt"]["x"]
    #         y0 = item["tick_pt"]["y"]
    #         drawrectangle(img, x0-5,y0-5,10,10)

    # for text_bb in gt_dic["input"]["task5_output"]["legend_pairs"]:
    #     x0 = text_bb["bb"]["x0"]
    #     y0 = text_bb["bb"]["y0"]
    #     width = text_bb["bb"]["width"]
    #     height = text_bb["bb"]["height"]
    #     drawrectangle(img, x0,y0,width,height)

    ## You could comment the following and add the cv2.imwrite("path/to/file.png", img) to save the img
    ## Rather then showing it.

    # cv2.imshow("gt_bb", img)
    # cv2.waitKey(0)

    cv2.imwrite(images_file_name+"_gt_bb.png", img, BGR)

def drawrectangle(img,x0,y0,width,height,BGR, plot_bb):
    print("----------------");
    print(plot_bb);
    print(str(x0) + " - " + str(width));
    if( (plot_bb["X0"]-5 <= (x0) or  plot_bb["Y0"]-5 <= (y0) ) and (width <= (plot_bb["WIDTH"]+5) and height <= (plot_bb["HEIGHT"]+5))     ):
    #and (height < plot_bb["HEIGHT"]) and (plot_bb["Y0"] < y0 )):
        print("drawing rect..");
        return cv2.rectangle(img, (x0,480-y0),(width,480-height), BGR,1)
