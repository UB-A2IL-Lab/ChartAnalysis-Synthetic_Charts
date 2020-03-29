from datetime import datetime
from matplotlib import pyplot as plt
import random
import numpy as np
import os
import errno
import csv_read_write_utils as csv
import _plot_tick_charts as ticks_library;

from shutil import copyfile

def copy_file_from_to(src, dst):
    copyfile(src, dst)

plt.rcParams.update({'figure.max_open_warning': 0})


chartNum = 1;

def get_time_now():
    now = datetime.now() # current date and time
    date_time = now.strftime("%y%m%d_%H%M%S")
    return date_time

def str_list_to_int_list(str_list):
    n = 0
    while n < len(str_list):
        str_list[n] = int(str_list[n])
        n += 1
    return(str_list)

def create_dir(dirName):
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")

def write_log_file( data , output_folder_name):
     # ['ctype', 'independent_variable', 'dependent_variable', 'chart_title',  'x_label', 'y_label', 'font_size', 'line_style', 'line_width', 'x_ticks', 'y_ticks', 'bar_width', 'color_array', 'orientation', 'legendVisibility', 'chartNum', 'i_axis_visible', 'label_visible', 'output_folder_name'];



    values = [
            data['ChartNum'],
            data['Folder_Name'],
            data['File_Link'],
            data['Chart_Type'],
            data['Orientation'],
            data['Tick_Direction'], data['Tick_Length'], data['Tick_Width'], data['Tick_X_Axis_Major_Locator'],
            data['Tick_X_Axis_Minor_Locator'], data['Tick_X_Axis_Tick_Style'], data['Tick_X_Axis_Color'], data['Tick_X_Axis_Font_Name'], data['Tick_X_Axis_Font_Size'], data['Tick_X_Axis_Rotation'],
            data['Tick_Y_Axis_Major_Locator'], data['Tick_Y_Axis_Minor_Locator'], data['Tick_Y_Axis_Tick_Style'], data['Tick_Y_Axis_Color'], data['Tick_Y_Axis_Font_Name'], data['Tick_Y_Axis_Font_Size'], data['Tick_Y_Axis_Rotation'], data['ShowGrid'], data['Independent_Axis_Scale'],
            data['Independent_Axis_Labels_Source'], data['Dependent_Axis_Scale'], data['Dependent_Axis_Labels_Source'],
            ];

    csv.write_to_csv_line_by_line(output_folder_name + '//LOG_FILE.csv',values);


def plot_chart(ctype, x,y, chart_title, x_label, y_label, font_size, line_style, line_width,  x_ticks, y_ticks, bar_width, color_array, orientation, legendVisibility, legend_array, chartNum, i_axis_visible, label_visible, output_folder_name, tick_variety, showGrid, data):

    fig, ax = plt.subplots();

    #
    # csvData = [['ctype', 'independent_variable', 'dependent_variable', 'chart_title',  'x_label', 'y_label', 'font_size', 'line_style', 'line_width', 'x_ticks', 'y_ticks', 'bar_width', 'color_array', 'orientation', 'legendVisibility', 'chartNum', 'i_axis_visible', 'label_visible', 'output_folder_name'], [ctype, x, y, chart_title,  x_label, y_label, font_size, line_style, line_width, x_ticks, y_ticks, bar_width, color_array, orientation, legendVisibility, chartNum, i_axis_visible, label_visible, output_folder_name]];

    # summary_CSV_Data = [ctype, x, y, chart_title,  x_label, y_label, font_size, line_style, line_width, x_ticks, y_ticks, bar_width, color_array, orientation, legendVisibility, chartNum, i_axis_visible, label_visible, output_folder_name];



    if(label_visible == "FALSE"):
        for xlabel_i in plt.gca().axes.get_xticklabels():
            xlabel_i.set_visible(False);
        for ylabel_i in plt.gca().axes.get_yticklabels():
            ylabel_i.set_visible(False);

    if(orientation == 'Vertical'):
        ax.set_xlabel(x_label, fontsize=font_size)
        ax.set_ylabel(y_label, fontsize=font_size)
        # if(i_axis_visible == "TRUE"):
        #     plt.gca().axes.get_xaxis().set_visible(False);

    elif(orientation == 'Horizontal'):
        ax.set_xlabel(y_label, fontsize=font_size)
        ax.set_ylabel(x_label, fontsize=font_size)
        # if(i_axis_visible == "TRUE"):
        #     plt.gca().axes.get_yaxis().set_visible(False);

    ax.set_title(chart_title);
    ax.grid(showGrid);
    #ax.set_xticklabels( ('2011-Jan-4', '2011-Jan-5', '2011-Jan-6') )
    fig.tight_layout()


    print(chartNum);
    if(ctype == 'Line'):
        p1 = [None]*5
        # x_ticks = [int(numeric_string) for numeric_string in x_ticks]
        # x = np.linspace(0, x_ticks[len(x_ticks)-1],len(x_ticks))
        # x = np.linspace(1, len(x_ticks),len(x_ticks));
        x = np.arange(len(x_ticks));

        print(x);
        print("x for line ...", x);
        ax.set_xticklabels(x);

        for i,dependent_data in enumerate(y):
            if(orientation == 'Vertical'):
                if(i==0):
                    ax.set_xticks([p +  bar_width for p in x]);
                    ax.set_xticklabels(x_ticks);

                p1[i] = plt.plot(x,str_list_to_int_list(dependent_data), linestyle=line_style, linewidth=line_width, color=color_array[i], label=x_ticks)
            elif(orientation == 'Horizontal'):
                if(i==0):
                    ax.set_yticks([p +  bar_width for p in x]);
                    ax.set_yticklabels(x_ticks);

                p1[i] = plt.plot(str_list_to_int_list(dependent_data),x, linestyle=line_style, linewidth=line_width, color=color_array[i], label=y_ticks)
        if(legendVisibility == True):
            # plt.legend((p1[0][0], p1[1][0]),(legend_array[0], legend_array[1]));
            if(len(y)==2):
                plt.legend((p1[0][0], p1[1][0]),(legend_array[0], legend_array[1]));
            if(len(y)==3):
                plt.legend((p1[0][0], p1[1][0],p1[2][0]),(legend_array[0], legend_array[1],legend_array[2]));


        CHART_FOLDER = output_folder_name+"/Chart"+str(chartNum);
        #
        # create_dir(CHART_FOLDER);
        # print(CHART_FOLDER+ "/Chart"+str(chartNum));
        # create_dir(CHART_FOLDER+ "/Chart"+str(chartNum));
        if(tick_variety==True):
            print("tick_variety is true....");
            ticks_library.plot_ticks(CHART_FOLDER,output_folder_name,chartNum,plt, fig, ax, chart_title,  x_label, y_label, i_axis_visible, label_visible, data);
        else:
            plt.savefig(CHART_FOLDER + "/Chart"+str(chartNum)+".png");
            plt.savefig(CHART_FOLDER+ "/Chart"+str(chartNum)+".svg");
            # csv.write_csv(CHART_FOLDER + '//LOG_FILE.csv', csvData);

        # csv.write_csv_horizontally(output_folder_name + '//LOG_FILE.csv',csvData);

        # csv.append_to_csv(output_folder_name + '//Summary_Log_File.csv', summary_CSV_Data);
        # copy_file_from_to('./config.json',output_folder_name + '/config.json');
        plt.clf();
        return True;
    elif (ctype == 'Bar'):
        # x = np.linspace(0, 4,4)
        # print(x);
        # x_ticks = [int(numeric_string) for numeric_string in x_ticks]
        # x = np.linspace(0, x_ticks[len(x_ticks)-1],len(x_ticks))
        # x = np.linspace(1, len(x_ticks),len(x_ticks));
        x = np.arange(len(x_ticks));
        # x = np.linspace(0,len(x_ticks),len(x_ticks));
        print(x_ticks);
        print(len(x_ticks));
        print(x);

        p1 = [None]*5
        print("x for bar ...", x);

        numOfDependentVars = len(y);
        print("numOfDependentVars = ",numOfDependentVars);
        # ax.set_xticks(x);

        # x = x - (bar_width*numOfDependentVars)/2;
        for i,dependent_data in enumerate(y):
            if(orientation == 'Vertical'):
                # ax.set_xticks(x);
                # ax.set_xticklabels(x_ticks);
                if(i==0):
                    ax.set_xticks([p +  bar_width for p in x]);
                    ax.set_xticklabels(x_ticks);

                p1[i] = plt.bar(x,str_list_to_int_list(dependent_data), width=bar_width, color=color_array[i],label=x_ticks)

            elif(orientation == 'Horizontal'):
                if(i==0):
                    ax.set_yticks([p +  bar_width for p in x]);
                    ax.set_yticklabels(x_ticks);

                p1[i] = plt.barh(x,str_list_to_int_list(dependent_data), height=bar_width, color=color_array[i], label = y_ticks )

            x = x + (bar_width);

        if(legendVisibility == True):
            if(len(y)==2):
                plt.legend((p1[0][0], p1[1][0]),(legend_array[0], legend_array[1]));
            if(len(y)==3):
                plt.legend((p1[0][0], p1[1][0],p1[2][0]),(legend_array[0], legend_array[1],legend_array[2]));


        CHART_FOLDER = output_folder_name+"/Chart"+str(chartNum);
        # create_dir(CHART_FOLDER);

        if(tick_variety==True):
            print("tick_variety is true....");
            ticks_library.plot_ticks(CHART_FOLDER,output_folder_name,chartNum,plt, fig, ax, chart_title,  x_label, y_label, i_axis_visible, label_visible, data);
        else:
            plt.savefig(CHART_FOLDER + "/Chart"+str(chartNum)+".png");
            plt.savefig(CHART_FOLDER+ "/Chart"+str(chartNum)+".svg");
            # csv.write_csv(CHART_FOLDER + '//LOG_FILE.csv', csvData);
            # plt.savefig(CHART_FOLDER + "/Chart"+str(chartNum)+".svg")
        # csv.write_csv(CHART_FOLDER + '//LOG_FILE.csv', csvData);
        # csv.write_csv_horizontally(output_folder_name + '//LOG_FILE.csv',csvData);

        # csv.append_to_csv(output_folder_name + '//Summary_Log_File.csv', summary_CSV_Data);
        # copy_file_from_to('./config.json',output_folder_name + '/config.json');
        plt.clf();
        return True;
    elif (ctype == 'Scatter'):
        # x = np.linspace(0, 4,4)
        p1 = [None]*5
        # x_ticks = [int(numeric_string) for numeric_string in x_ticks]
        # x = np.linspace(0, x_ticks[len(x_ticks)-1],len(x_ticks))
        # x = np.linspace(1, len(x_ticks),len(x_ticks));
        x = np.arange(len(x_ticks));
        print(x);
        print("x for scatter ...", x);
        ax.set_xticklabels(x)

        for i,dependent_data in enumerate(y):
            if(orientation == 'Vertical'):
                p1[i] = plt.scatter(x, str_list_to_int_list(dependent_data), c=color_array[i], alpha=0.5);
            elif(orientation == 'Horizontal'):
                p1[i] = plt.scatter(str_list_to_int_list(dependent_data),x, c=color_array[i], alpha=0.5);

            if(legendVisibility == True):
                #plt.legend((p1[0][0], p1[1][0]),(legend_array[0], legend_array[1]));
                plt.legend();

            CHART_FOLDER = output_folder_name+"/Chart"+str(chartNum);
            # create_dir(CHART_FOLDER);


            if(tick_variety==True):
                print("tick_variety is true....");
                ticks_library.plot_ticks(CHART_FOLDER,output_folder_name,chartNum,plt, fig, ax, chart_title,  x_label, y_label,i_axis_visible, label_visible, data);
            else:
                plt.savefig(CHART_FOLDER + "/Chart"+str(chartNum)+".png");
                plt.savefig(CHART_FOLDER+ "/Chart"+str(chartNum)+".svg");

            # csv.write_csv(CHART_FOLDER + '//LOG_FILE.csv', csvData);
            # csv.write_csv_horizontally(output_folder_name + '//LOG_FILE.csv',csvData);

            # csv.append_to_csv(output_folder_name + '//Summary_Log_File.csv', summary_CSV_Data);
            # copy_file_from_to('./config.json',output_folder_name + '/config.json');
            plt.clf();
            return True;
