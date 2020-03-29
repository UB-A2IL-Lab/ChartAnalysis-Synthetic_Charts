import json
import matplotlib.gridspec as gridspec
import csv_read_write_utils as csv
import utils as utils

with open('config.json') as f:
  config = json.load(f)

with open('config_default.json') as f:
  configDefault = json.load(f)

#read config file parameters
#passing the default value in second parameter
chart_type = config.get('Type') or configDefault.get('Type');

print("chart_type = "+str(chart_type));
tick_variety = config.get('Tick_Variety') or configDefault.get('Tick_Variety');

# font_size = config['Text_Font']['Font_Size'];
#passing the default value in second parameter
font_size = config.get('Text_Font').get('Font_Size') or configDefault.get('Text_Font').get('Font_Size');
print(font_size);

independent_axes_scale = config['Independent_Axes']['Scale'][0];
dependent_axis_1_scale = config['Dependent_Axis_1']['Scale'][0];

independent_axes_source = 'DATAFILE-DATA';
dependent_axes_source = 'DATAFILE-DATA';

line_style = config['Chart_Type_Specific']['Line']['Line_Style'] or configDefault['Chart_Type_Specific']['Line']['Line_Style'];
line_width = config['Chart_Type_Specific']['Line']['Line_Width'] or configDefault['Chart_Type_Specific']['Line']['Line_Width'];
bar_width = config['Chart_Type_Specific']['Bar']['Bar_Width'] or configDefault['Chart_Type_Specific']['Bar']['Bar_Width'];
color_array = config['Data']['Color']['Random'] or configDefault['Data']['Color']['Random'];
orientation_array = config['Orientation'] or configDefault['Orientation'];
legend_visibility_array = config['Legend_Visibility']['Visible'] or configDefault['Legend_Visibility']['Visible'];
independent_axes_visible_array = config['Independent_Axes']['Visible'] or configDefault['Independent_Axes']['Visible'];
labels_visible_array = config['Independent_Axes']['Labels_Visible'] or configDefault['Independent_Axes']['Labels_Visible'];
showgrid_array = config['ShowGrid'] or configDefault['ShowGrid'];
#read csv data
filenames_array = ['csv_format_data_2.csv'];
#,'csv_format_data_2.csv'];

for filename in filenames_array:
    csvData = csv.read_csv(filename);
    output_folder_name = "SynChart_" + utils.get_time_now();
    utils.create_dir(output_folder_name);
    utils.copy_file_from_to('./config.json',output_folder_name + '/config.json');
    utils.copy_file_from_to('./_tick_config_mini.json',output_folder_name + '/_tick_config_mini.json');

    #read CSV parameters
    independent_variable = csvData['i_data'];
    independent_variable =  csvData['i_axis_labels'];
    chart_title = csvData['graph_title'];
    x_ticks = csvData['i_axis_labels'];
    y_ticks = csvData['d_axis_labels'];
    x_label = csvData['i_axis_title'];
    y_label = csvData['d_axis_title'];
    legend_array = csvData['d_label'];
    # print("x_label = "+x_label);
    # print("y_label = "+y_label);


    dependent_variable = csvData['d_data'];

    chartNum = 1;
    all_CSV_Data = [];
    for label_visible in labels_visible_array:
        for i_axis_visible in independent_axes_visible_array:
            for legendVisible in legend_visibility_array:
                for showGrid  in showgrid_array:
                    for orientation in orientation_array:
                        for ctype in chart_type:
                            data = {

                                    'Folder_Name' : output_folder_name,
                                    'Chart_Type' : ctype,
                                    'Orientation': orientation,
                                    'Tick_Direction': '',
                                    'Tick_Length' : '' ,
                                    'Tick_Width' : '' ,
                                    'Tick_X_Axis_Major_Locator' : '' ,
                                    'Tick_X_Axis_Minor_Locator' : '' ,
                                    'Tick_X_Axis_Tick_Style' : '',
                                    'Tick_X_Axis_Color' : '',
                                    'Tick_X_Axis_Font_Name' : '',
                                    'Tick_X_Axis_Font_Size' : '',
                                    'Tick_X_Axis_Rotation' : '',
                                    'Tick_Y_Axis_Major_Locator' : '',
                                    'Tick_Y_Axis_Minor_Locator' : '',
                                    'Tick_Y_Axis_Tick_Style' : '',
                                    'Tick_Y_Axis_Color' : '',
                                    'Tick_Y_Axis_Font_Name' : '',
                                    'Tick_Y_Axis_Font_Size' : '',
                                    'Tick_Y_Axis_Rotation' : '',
                                    'ShowGrid' : showGrid,
                                    'Independent_Axis_Scale' : independent_axes_scale,
                                    'Independent_Axis_Labels_Source' : independent_axes_source,
                                    'Dependent_Axis_Scale' : dependent_axis_1_scale,
                                    'Dependent_Axis_Labels_Source': dependent_axes_source
                                    } ;

                            response = utils.plot_chart(ctype, independent_variable, dependent_variable, chart_title,  x_label, y_label, font_size, line_style, line_width, x_ticks, y_ticks, bar_width, color_array, orientation, legendVisible, legend_array,chartNum, i_axis_visible, label_visible, output_folder_name, tick_variety, showGrid, data);
                            if(response == True):
                                chartNum = chartNum + 1;
