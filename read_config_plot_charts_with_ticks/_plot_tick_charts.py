# importing required modules
import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from PIL import Image
import os
import _write_ground_truth as gt
import verify_gt_bb as plot_gt
import utils as utils

os.environ['TK_SILENCE_DEPRECATION'] = '1'

from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

def plot_ticks(folderName,output_folder_name,chartNum,plt,  fig, ax,  chart_title,  x_label, y_label, i_axis_visible, label_visible , data):


    with open('_tick_config_mini.json') as f:
      configNew = json.load(f)

    plot_tick = configNew.get('PLOT_TICK');
    directions_array = plot_tick.get('DIRECTION' );
    length_array = plot_tick.get('LENGTH' );
    width_array = plot_tick.get('WIDTH' );

    x_axis = plot_tick.get('X_AXIS');
    x_major_locator_array =  x_axis.get('MAJOR_LOCATOR' );
    x_minor_locator_array =  x_axis.get('MINOR_LOCATOR' );
    x_which_array = x_axis.get('TICK_STYLE_IN_OUT' );
    x_color_array = x_axis.get('COLOR');
    x_font = x_axis.get("FONT");
    x_font_name_array = x_font.get("NAME");
    x_font_size_array = x_font.get("SIZE");
    x_rotation_array = x_axis.get("ROTATION");

    y_axis = plot_tick.get('Y_AXIS')
    y_major_locator_array =  y_axis.get('MAJOR_LOCATOR' );
    y_minor_locator_array =  y_axis.get('MINOR_LOCATOR' );
    y_which_array = y_axis.get('TICK_STYLE_IN_OUT' );
    y_color_array = y_axis.get('COLOR' );
    y_font = y_axis.get("FONT");
    y_font_name_array = y_font.get("NAME");
    y_font_size_array = y_font.get("SIZE");
    y_rotation_array = y_axis.get("ROTATION");


    i = utils.chartNum;

    for y_major_locator in y_major_locator_array:
        for y_minor_locator in y_minor_locator_array:
            for y_which in y_which_array:
                for y_color in y_color_array:
                    for y_font_name in y_font_name_array:
                        for y_font_size in y_font_size_array:
                            for y_rotation in y_rotation_array:
                                for x_major_locator in x_major_locator_array:
                                    for x_minor_locator in x_minor_locator_array:
                                        for x_which in x_which_array:
                                            for x_color in x_color_array:
                                                for x_font_name in x_font_name_array:
                                                    for x_font_size in x_font_size_array:
                                                        for x_rotation in x_rotation_array:
                                                            for width in width_array:
                                                                for length in length_array:
                                                                    for direction in directions_array:
                                                                        # ax.xaxis.set_minor_locator(MultipleLocator(x_minor_locator))
                                                                        # ax.xaxis.set_major_locator(MultipleLocator(x_major_locator))

                                                                        # ax.yaxis.set_minor_locator(MultipleLocator(y_minor_locator))
                                                                        # ax.yaxis.set_major_locator(MultipleLocator(y_major_locator))

                                                                        plt.tick_params(axis='x', colors=x_color, direction=direction, which = x_which, length=length, width=width )
                                                                        plt.tick_params(axis='y', colors=y_color, direction=direction, which = x_which, length=length, width=width)
                                                                        plt.xticks(fontname = x_font_name, fontsize = x_font_size, rotation = x_rotation)
                                                                        plt.yticks(fontname = y_font_name, fontsize = y_font_size, rotation = y_rotation)
                                                                        fig.tight_layout();

                                                                        directoryName = output_folder_name+"/Chart" +str(i);
                                                                        utils.create_dir(directoryName);
                                                                        data['ChartNum'] = 'Chart' + str(utils.chartNum);

                                                                        plt.savefig(directoryName+'/'+data['ChartNum']+'.png');

                                                                        gt.create_ground_truth_json(plt, ax,  fig,data['ChartNum'], directoryName, chart_title, x_label, y_label, i_axis_visible, label_visible);


                                                                        plot_gt.verify(directoryName+'/'+data['ChartNum'],directoryName+'/'+data['ChartNum']);
                                                                        plt.savefig(directoryName+ "/Chart"+str(i)+".svg");



                                                                        data['File_Link'] = "=hyperlink(\""+"./"+"Chart"+str(i)+'/'+data['ChartNum']+'_gt_bb.png'+"\")";
                                                                        data['Tick_Direction'] = direction;
                                                                        data['Tick_Length'] = length ;
                                                                        data['Tick_Width'] = width ;
                                                                        data['Tick_X_Axis_Major_Locator'] = x_major_locator ;
                                                                        data['Tick_X_Axis_Minor_Locator'] = x_minor_locator ;
                                                                        data['Tick_X_Axis_Tick_Style'] = x_which;
                                                                        data['Tick_X_Axis_Color'] = x_color;
                                                                        data['Tick_X_Axis_Font_Name'] = x_font_name;
                                                                        data['Tick_X_Axis_Font_Size'] = x_font_size;
                                                                        data['Tick_X_Axis_Rotation'] = x_rotation;
                                                                        data['Tick_Y_Axis_Major_Locator'] = y_major_locator;
                                                                        data['Tick_Y_Axis_Minor_Locator'] = y_minor_locator;
                                                                        data['Tick_Y_Axis_Tick_Style'] = y_which;
                                                                        data['Tick_Y_Axis_Color'] = y_color;
                                                                        data['Tick_Y_Axis_Font_Name'] = y_font_name;
                                                                        data['Tick_Y_Axis_Font_Size'] = y_font_size;
                                                                        data['Tick_Y_Axis_Rotation'] = y_rotation;

                                                                        utils.write_log_file(data, output_folder_name);
                                                                        i=i+1;
                                                                        utils.chartNum = i;
